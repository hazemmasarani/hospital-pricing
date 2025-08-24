import os
import sqlite3
import pandas as pd
from src.config import DB_PATH

# Step 0: Delete DataBase
def delete_database():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

# Step 1: Create schema if not exists
def create_schema():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS hospital_prices (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                hospital_name TEXT,
                state TEXT,
                county TEXT,
                procedure_name TEXT,
                code TEXT,
                code_type TEXT,
                setting TEXT,
                cash_price REAL,
                cash_discount REAL,
                payer TEXT,
                plan TEXT,
                allowed_amount REAL,
                min_negotiated_price REAL,
                max_negotiated_price REAL,
                rate_type TEXT
            )
        """)
        conn.commit()

# Step 2: Save DataFrame to database
def save_dataframe(df: pd.DataFrame, required_columns: list):
    with sqlite3.connect(DB_PATH) as conn:
        # Ensure DataFrame contains only required columns
        df_to_save = df[required_columns]
        df_to_save.to_sql("hospital_prices", conn, if_exists="append", index=False)
        conn.commit()