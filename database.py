import sqlite3

# Connect to the SQLite database
def create_connection():
    conn = sqlite3.connect("reminder_management.db")
    return conn

#initializing the database
def initialize_db():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS reminders (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        description TEXT,
                        due_date TEXT)''')
    conn.commit()
    conn.close()