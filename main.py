from modules.folder import (
    create_directory, 
    remove_temporary_directory, 
    process_files, 
    load_data_into_db
)

from config_db import db_schema

def main():
    csv_directory = 'data/{schema}'
    ini_file = 'data/{schema}/{schema}.ini'
    processed_folder = 'temp/{schema}/processed'
    schema = 'taxes'

    # Remove the temporary directory before processing the files
    remove_temporary_directory('temp/purchases')

    # Process the files
    create_directory(processed_folder)
    process_files(csv_directory, ini_file, processed_folder)

    # Load the data into the database
    load_data_into_db(schema, processed_folder)
    
if __name__ == '__main__':    
    main()
