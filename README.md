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
   db_schema = 'test'
   ```

2. Ensure that the PostgreSQL database is running and that the credentials provided in the `config_db.py` file are correct.

    Remember to create the schema in the PostgreSQL database if it does not exist.

3. After configuring the above parameters, run the script to start processing the CSV files. In case of errors, problematic files will be moved to the `temp/processed` folder and errors logged in the `error-log.csv` file.

## Usage 🚀

To use the Text To DB Converter, follow these steps:

1. Open your command line interface (CLI).
2. Navigate to the directory where the `main.py` file is located.
3. Run the following command:

   ```bash
   python main.py
   ```

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) for details.
