import pandas as pd
from pathlib import Path
from src.config import DATA_RAW

def parse_file(file_name, needed_columns, columns_names=None, skiprows=0):
    """
    Reads a hospital price file and returns only the needed columns.

    Args:
        file_name (str or Path): Name of the file to parse (relative to DATA_RAW).
        needed_columns (list): List of columns to keep in the dataframe.
        columns_names (list, optional): List of column names to use when reading the file.
        skiprows (int): Number of lines to skip at the start of the CSV file.

    Returns:
        pd.DataFrame: Cleaned dataframe containing only the required columns.
    """
    file_path = Path(DATA_RAW) / file_name

    # Detect file type and read accordingly
    if file_path.suffix.lower() == '.csv':
        df = pd.read_csv(file_path, skiprows=skiprows, names=columns_names if columns_names else None, header=0 if not columns_names else None)
    elif file_path.suffix.lower() in ['.xlsx', '.xls']:
        df = pd.read_excel(file_path)
    elif file_path.suffix.lower() == '.json':
        df = pd.read_json(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_path.suffix}")

    # Keep only the needed columns if they exist
    missing = [col for col in needed_columns if col not in df.columns]
    if missing:
        print(f"Warning: Missing columns in {file_name}: {missing}")

    return df[[col for col in needed_columns if col in df.columns]]
