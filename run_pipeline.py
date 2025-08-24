import sys
import traceback
from src.config import HOSPITALS, SAVED_COLUMNS
from src.downloader import download_all_files
from src.parser import parse_file
from src.reconciler import set_attributes
from src.database import create_schema, delete_database, save_dataframe

def run_pipeline():
    
    print("[STEP 0] Deleting existing database if any...")
    delete_database()

    print("[STEP 1] Creating database schema...")
    create_schema()

    print("[STEP 2] Downloading hospital files...")
    download_all_files()

    print("[STEP 3] Parsing and saving data...")
    for hospital in HOSPITALS:
        try:
            print(f"[INFO] Processing: {hospital['file_name']}")
            df = parse_file(
                file_name=hospital["file_name"],
                needed_columns=SAVED_COLUMNS,
                columns_names=hospital.get("columns_names"),
                skiprows=hospital.get("skip_rows", 0)
            )
            df = set_attributes(df, hospital.get("db_cols_mapper", {}))
            save_dataframe(df, SAVED_COLUMNS)
            print(f"[SUCCESS] Saved data for: {hospital['file_name']}")
        except Exception as e:
            print(f"[ERROR] Failed for {hospital['file_name']}: {e}")
            traceback.print_exc(file=sys.stdout)

if __name__ == "__main__":
    run_pipeline()