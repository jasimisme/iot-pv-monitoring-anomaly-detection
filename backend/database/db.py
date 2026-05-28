import sqlite3
import os


# =====================================================
# Base Directory
# =====================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)


# =====================================================
# Database Path
# =====================================================

DATABASE_PATH = os.path.join(
    BASE_DIR,
    "storage",
    "pv_monitor.db"
)


# =====================================================
# Connect Database
# =====================================================

def connect_db():

    conn = sqlite3.connect(DATABASE_PATH)

    conn.row_factory = sqlite3.Row

    return conn


# =====================================================
# Create Tables
# =====================================================

def create_tables():

    conn = connect_db()

    cursor = conn.cursor()

    # ================================================
    # Telemetry Table
    # ================================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS telemetry (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        voltage REAL,

        current REAL,

        temperature REAL,

        irradiance REAL,

        timestamp TEXT
    )
    """)

    # ================================================
    # Anomaly Logs Table
    # ================================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS anomaly_logs (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        fault TEXT,

        confidence REAL,

        timestamp TEXT
    )
    """)

    conn.commit()

    conn.close()

    print("Database initialized successfully.")


# =====================================================
# Main
# =====================================================

if __name__ == "__main__":

    create_tables()