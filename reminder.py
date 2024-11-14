from database import create_connection

# Add a new reminder
def add_reminder(description, due_date):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reminders (description, due_date) VALUES (?, ?)", (description, due_date))
    conn.commit()
    conn.close()

    # View all reminders
    def view_reminders():
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM reminders")
        reminders = cursor.fetchall()
        conn.close()
        return reminders

        # Update a reminder by ID
    def update_reminder(reminder_id, new_description, new_due_date):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE reminders SET description = ?, due_date = ? WHERE id = ?",
                       (new_description, new_due_date, reminder_id))
        conn.commit()
        conn.close()

    # Delete a reminder by ID
    def delete_reminder(reminder_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM reminders WHERE id = ?", (reminder_id,))
        conn.commit()
        conn.close()