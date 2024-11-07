from database import create_connection

# Add a new reminder
def add_reminder(description, due_date):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reminders (description, due_date) VALUES (?, ?)", (description, due_date))
    conn.commit()
    conn.close()