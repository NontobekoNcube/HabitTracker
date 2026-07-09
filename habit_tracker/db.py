import sqlite3
from datetime import date

def get_connection():
    conn = sqlite3.connect("habits.db") #connects to habits.db file
    return conn

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISITS habits(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   periodicity TEXT,
                   target_period INTEGER,
                   creationdate TEXT)
                   """)
    
    cursor.execute("""
                   CREATE  TABLE IF NOT EXISTS completions(
                   completion_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   habit_id INTEGER NOT NULL,
                   date TEXT NOT NULL,
                   FOREIGN KEY (habit_id) REFERENCES habits(id)
                   )
                   """)
    
    conn.commit()
    conn.close()
    
        