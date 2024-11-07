import sqlite3

# Connect to the SQLite database
def create_connection():
    conn = sqlite3.connect("reminder_management.db")
    return conn

