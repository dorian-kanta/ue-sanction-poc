import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = "data/sanctions.sqlite"

def init_db():
    Path("data").mkdir(exist_ok=True)  # Crée le dossier s’il n’existe pas
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sanctions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            program TEXT,
            updated_at TEXT
        )
    """)
    conn.commit()
    return conn

def get_all_sanctions(conn):
    return pd.read_sql_query("SELECT name, program FROM sanctions", conn)