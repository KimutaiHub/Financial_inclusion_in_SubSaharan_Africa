import sqlite3
import pandas as pd
from pathlib import Path

db_path = Path("data_raw/database.sqlite")
out_dir = Path("data_clean")
out_dir.mkdir(exist_ok=True)

conn = sqlite3.connect(db_path)

tables_to_extract = ["Country", "Indicators", "Series"]

for table in tables_to_extract:
    df = pd.read_sql(f"SELECT * FROM {table};", conn)
    out_path = out_dir / f"{table}.csv"
    df.to_csv(out_path, index=False)
    print(f"Exported {table} -> {out_path}")

conn.close()
print("Extraction complete.")
