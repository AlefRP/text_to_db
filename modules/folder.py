import os
import shutil
from processing import load_column_mapping, replace_columns_in_csvs
from db_load import create_database_manager

def create_directory(directory):
    """Creates the specified directory if it does not exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def remove_temporary_directory(directory):
    """Removes the specified directory and its contents."""
    if os.path.exists(directory):
        shutil.rmtree(directory)

def process_files(csv_directory, ini_file, processed_folder):
    """Processes the CSV files and saves the treated files in the specified folder."""
    mapping = load_column_mapping(ini_file)
    replace_columns_in_csvs(csv_directory, mapping, processed_folder)

def load_data_into_db(schema, processed_folder):
    """Creates the database manager and loads the data into the database."""
    create_database_manager(schema, processed_folder)