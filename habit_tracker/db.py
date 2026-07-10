import sqlite3
from datetime import date

def get_connection():
    conn = sqlite3.connect("habits.db") #connects to habits.db file
    return conn

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS habits(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   periodicity TEXT,
                   target_period INTEGER,
                   creation_date TEXT)
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
    
    def save_habit(habit):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
                       INSERT INTO habits (name, periodicity, target_period, creation_date)
                       VALUES (?, ?, ?, ?)""", # sql code with placeholder values
                       (habit.name, habit.periodicity, habit.target_period, str(habit.creation_date))) # tuple containing actual values to insert
        habit.id = cursor.lastrowid # automatic assignment of the last row number as the ID of the new inserted row, now habit.id has a value and is not None anymore! 
        conn.commit() #saves changes to habits.db
        conn.close()
        
        