import pandas as pd

def filter_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Returns a DataFrame with only the columns specified in the list.
    Ignores columns not present in the DataFrame.
    """
    existing_columns = [col for col in columns if col in df.columns]
    return df[existing_columns]

def set_attributes(df: pd.DataFrame, attributes: dict) -> pd.DataFrame:
    """
    Sets the given attributes (column name and value) for all rows in the DataFrame.
    Adds columns if they do not exist.
    """
    for attr, value in attributes.items():
        df[attr] = value
    return df