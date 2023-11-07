import os
import shutil
from tqdm import tqdm

def load_column_mapping(ini_file):
    '''
    Loads the column mapping from the .ini file.
    '''
    mapping = {}
    with open(ini_file, 'r', encoding='ISO-8859-1') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('['):
                column_name, code = line.split('=')
                mapping[code] = column_name
    return mapping

def replace_columns_in_csvs(csv_directory, mapping, processed_folder):
    '''
    Replaces the codes with the column names in CSV files.
    '''
    files = [file for file in os.listdir(csv_directory) if file.endswith('.csv')]
    for file in tqdm(files, desc='Processing CSV files'):
        csv_file = os.path.join(csv_directory, file)
        processed_file = os.path.join(processed_folder, file)
        
        with open(csv_file, 'r', encoding='ISO-8859-1', errors='replace') as f_in, \
             open(processed_file, 'w', encoding='ISO-8859-1') as f_out:
            
            line = f_in.readline()
            for code, column_name in mapping.items():
                line = line.replace(code, column_name)
            f_out.write(line)
            
            shutil.copyfileobj(f_in, f_out)