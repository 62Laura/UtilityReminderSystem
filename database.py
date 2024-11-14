import sqlite3

class Database:
    def __init__(self, db_name="reminder_management.db"):
        self.db_name = db_name

    # Connect to the SQLite database
    def create_connection(self):
        return sqlite3.connect(self.db_name)
