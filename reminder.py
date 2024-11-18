# reminder.py

from database import Database

class Reminder:
    def _init_(self, description, due_date, reminder_id=None):
        self.description = description
        self.due_date = due_date
        self.reminder_id = reminder_id
        self.db = Database()

   # Add a new reminder
    def add_reminder(self):
        conn = self.db.create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO reminders (description, due_date) VALUES (?, ?)", (self.description, self.due_date))
        conn.commit()
        conn.close()

    # View all reminders
    @classmethod
    def view_reminders(cls):
        db = Database()  # Create a Database object
        conn = db.create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM reminders")
        reminders = cursor.fetchall()
        conn.close()
        return reminders

    # Update a reminder by ID
    def update_reminder(self, new_description, new_due_date):
        conn = self.db.create_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE reminders SET description = ?, due_date = ? WHERE id = ?",
                       (new_description, new_due_date, self.reminder_id))
        conn.commit()
        conn.close()

    # Delete a reminder by ID
    def delete_reminder(self):
        conn = self.db.create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM reminders WHERE id = ?", (self.reminder_id,))
        conn.commit()
        conn.close()