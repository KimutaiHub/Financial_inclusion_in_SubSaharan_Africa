import sqlite3
import pandas as pd
from pathlib import Path

db_path = Path("data_raw/database.sqlite")

if not db_path.exists():
    raise FileNotFoundError(f"Cannot find: {db_path.resolve()}")

conn = sqlite3.connect(db_path)

tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)
print("Tables in database.sqlite:")
print(tables.to_string(index=False))

conn.close()
