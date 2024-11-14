from reminder import Reminder
from scheduler import ReminderScheduler
from database import Database

def display_menu():
    print("1. Add Reminder")
    print("2. View Reminders")
    print("3. Update Reminder")
    print("4. Delete Reminder")
    print("5. Exit")

    def main():
        db = Database("reminders.db")
        db.initialize_db()  # Initialize the database
        scheduler = ReminderScheduler()  # Initialize the scheduler
        scheduler.start_scheduler()  # Start the reminder scheduler in a new thread

        while True:
            display_menu()
            choice = input("Choose an option: ")

            if choice == '1':
                description = input("Enter reminder description: ")
                due_date = input("Enter due date (YYYY-MM-DD HH:MM): ")
                reminder = Reminder(description, due_date)
                reminder.add_reminder()
                print("Reminder added successfully!")

                elif choice == '2':
                reminders = Reminder.view_reminders()
                for reminder in reminders:
                    print(f"ID: {reminder[0]}, Description: {reminder[1]}, Due Date: {reminder[2]}")

           elif choice == '3':
            reminder_id = int(input("Enter reminder ID to update: "))
            new_description = input("Enter new description: ")
            new_due_date = input("Enter new due date (YYYY-MM-DD HH:MM): ")
            reminder = Reminder(new_description, new_due_date, reminder_id)
            reminder.update_reminder(new_description, new_due_date)
            print("Reminder updated successfully!")