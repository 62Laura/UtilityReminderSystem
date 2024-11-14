import sqlite3

class Database:
    def __init__(self, db_name="reminder_management.db"):
        self.db_name = db_name
        
    # Connect to the SQLite database
    def create_connection(self):
        return sqlite3.connect(self.db_name)
      
# Initialize the database with a reminders table
    def initialize_db(self):
        conn = self.create_connection()
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS reminders (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            description TEXT,
                            due_date TEXT
                          )''')
        conn.commit()
        conn.close()
