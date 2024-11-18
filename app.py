from reminder import Reminder
from scheduler import ReminderScheduler
from database import Database

# Display the main menu
def display_menu():
    print("1. Add Reminder")
    print("2. View Reminders")
    print("3. Update Reminder")
    print("4. Delete Reminder")
    print("5. Exit")

# Main function to handle user interaction
def main():
    db = Database("reminders.db")
    db.initialize_db()  # Initialize the database
    scheduler = ReminderScheduler()  # Initialize the scheduler
    scheduler.start_scheduler()  # Start the reminder scheduler in a new thread

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':  # Add a new reminder
            description = input("Enter reminder description: ")
            due_date = input("Enter due date (YYYY-MM-DD HH:MM): ")
            reminder = Reminder(description, due_date)
            reminder.add_reminder()
            print("Reminder added successfully!")

        elif choice == '2':  # View all reminders
            reminders = Reminder.view_reminders()
            for reminder in reminders:
                print(f"ID: {reminder[0]}, Description: {reminder[1]}, Due Date: {reminder[2]}")

        elif choice == '3':  # Update a reminder
            reminder_id = int(input("Enter reminder ID to update: "))
            new_description = input("Enter new description: ")
            new_due_date = input("Enter new due date (YYYY-MM-DD HH:MM): ")
            reminder = Reminder(new_description, new_due_date, reminder_id)
            reminder.update_reminder(new_description, new_due_date)
            print("Reminder updated successfully!")

        elif choice == '4':  # Delete a reminder
            reminder_id = int(input("Enter reminder ID to delete: "))
            reminder = Reminder("", "", reminder_id)
            reminder.delete_reminder()
            print("Reminder deleted successfully!")

        elif choice == '5':  # Exit the application
            print("Exiting the application.")
            break

        else:  # Handle invalid choices
            print("Invalid choice. Please try again.")

# Run the application
if __name__ == "__main__":
    main()
