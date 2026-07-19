import sqlite3
from datetime import date
from habit_tracker import Habit

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
            VALUES (?, ?, ?, ?)""", 
            (habit.name, habit.periodicity, habit.target_period, str(habit.creation_date)))
    habit.id = cursor.lastrowid # automatic assignment of the last row number as the ID of the new inserted row, now habit.id has a value and is not None anymore! 
    conn.commit() #saves changes to habits.db
    conn.close()

def load_from_db(habit):
    conn = get_connection() #opens connection to habits.db
    cursor = conn.cursor()  #cursor is a tool to run SQL commands on the database

    cursor.execute("SELECT * FROM habits") #runs SQL command to select all rows from the habits table
    rows = cursor.fetchall() #fetches all rows from the habits table, returns list of tuples, each tuple is a row in the table

    habits = []
    for row in rows:
        # row = (id, name, periodicity, target_period, creation_date
        habit = Habit(row[1], row[2], row[3]) #reconstruct habit object from row
        habit.id = row[0] #set the id of the habit object to the id from the database
        habit.creation_date = date.fromisoformat(row[4]) 
        habits.append(habit)
    
    conn.close()
    return habits

def delete_habit(habit_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM habits WHERE id = ?", (habit_id,))
    conn.commit()
    conn.close()
        
def save_completion(habit_id, completion_date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO completions (habit_id, date)
            VALUES (?, ?)""", 
            (habit_id, str(completion_date)))
    conn.commit()
    conn.close()