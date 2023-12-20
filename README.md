# Text To DB Converter

## Overview 📈

This utility is designed to process CSV files containing tax data, translate the column names based on a provided dictionary, and then load the processed data into a PostgreSQL database. If errors occur during processing, the problematic files are recorded in an `error-log.csv` for subsequent review.

<img src="https://github.com/AlefRP/text_to_db/blob/main/images/TextToDBConverter.png" style="max-width: 100%; height: auto; border-radius: 10px;" alt="Overview of Text To DB Converter">

## Requirements 🐍

- Python 3.11.5
- Libraries: `pandas`, `sqlalchemy`, `csv`, `os`, `shutil`, `tqdm`

## Configuration ⚙️

1. Database credentials should be set up in the `config_db.py` file:

   ```python
   db_username = 'your_username'
   db_password = 'your_password'
   db_host = 'db_host'
   db_port = 'db_port'
   db_name = 'db_name'

2. Configure the data directory, tax configuration file, processed data folder, and schema in the main script as follows:

    ```python
    csv_directory = 'data/taxes/tax_extraction_17042023'
    ini_file = 'data/taxes/tax_extraction_17042023/taxes.ini'
    processed_folder = 'temp/taxes/processed'
    schema = 'taxes'
    ```

3. Ensure that the PostgreSQL database is running and that the credentials provided in the `config_db.py` file are correct.

    Remember to create the `taxes` schema in the PostgreSQL database if it does not exist.

4. After configuring the above parameters, run the script to start processing the CSV files. In case of errors, problematic files will be moved to the `temp/processed` folder and errors logged in the `error-log.csv` file.

## License 📜

This project is licensed under the MIT License - see the LICENSE.md file for details.
