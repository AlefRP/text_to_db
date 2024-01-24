import os
from config_db import db_username, db_password, db_host, db_port, db_name
from sqlalchemy import create_engine, text
import pandas as pd
import csv

class DatabaseManager:
    """
    This class manages the database connection and provides methods
    to create schemas and save CSV files into the database.
    """

    def __init__(self, uri, schema):
        """
        Initializes the database manager with the provided URI and schema.
        
        :param uri: The database URI.
        :param schema: The schema in the database.
        """
        self.engine = create_engine(uri)
        self.schema = schema
        self.create_schema()
        self.error_log = []

    def create_schema(self):
        """
        Creates the schema in the database if it does not exist yet.
        """
        try:
            with self.engine.connect() as conn:
                conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {self.schema}"))
        except Exception as e:
            print(f"Failed to create schema: {e}")

    def infer_delimiter(self, filepath):
        """
        Infers the delimiter used in a CSV file.
        
        :param filepath: The path to the CSV file.
        :return: The delimiter used in the CSV file.
        """
        with open(filepath, 'r', encoding='ISO-8859-1') as file:
            sniffer = csv.Sniffer()
            try:
                dialect = sniffer.sniff(file.read(1024))
                return dialect.delimiter
            except csv.Error:
                error_message = f"Unable to determine the file delimiter {filepath}"
                print(error_message)
                self.error_log.append({'file': filepath, 'error': error_message})
                return None

    def save_csvs_to_database(self, folder):
        """
        Saves all CSV files from a folder into the database.
        
        :param folder: The folder containing the CSV files.
        """
        for filename in os.listdir(folder):
            if filename.endswith('.csv'):
                filepath = os.path.join(folder, filename)
                self.save_individual_csv_to_database(filepath)
        
        # After processing all files, write errors to a CSV
        self.write_error_log()

    def save_individual_csv_to_database(self, filepath):
        """
        Saves an individual CSV file into the database.
        
        :param filepath: The path to the CSV file.
        """
        delimiter = self.infer_delimiter(filepath)
        if delimiter is None:
            return

        try:
            dataframe = pd.read_csv(filepath, delimiter=delimiter, encoding='ISO-8859-1', quotechar="'", low_memory=False)
            dataframe.columns = dataframe.columns.str.strip()
        except pd.errors.ParserError as e:
            error_message = f"Failed to read {filepath} due to ParserError: {e}"
            print(error_message)
            self.error_log.append({'file': filepath, 'error': error_message})
            return

        table_name = os.path.splitext(os.path.basename(filepath))[0]
        dataframe.to_sql(
            name=table_name,
            con=self.engine,
            if_exists='replace',
            index=False,
            schema=self.schema
        )

    def write_error_log(self):
        """Writes the error log to a CSV file."""
        error_df = pd.DataFrame(self.error_log)
        error_df.to_csv('error_log.csv', index=False)

def create_database_manager(schema, folder):
    """
    Creates a database manager and saves the CSV files in the provided folder to the database.
    
    :param schema: The schema in the database.
    :param folder: The folder containing the CSV files.
    """
    uri = f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'
    database_manager = DatabaseManager(uri, schema)
    database_manager.save_csvs_to_database(folder)
