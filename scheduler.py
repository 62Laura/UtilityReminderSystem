import time
import threading
from reminder import Reminder
from datetime import datetime

class ReminderScheduler:
    def __init__(self):
        self.reminder_class = Reminder  # Reference to the Reminder class

    def reminder_scheduler(self):
        """Checks for due reminders and alerts."""
        while True:
            reminders = self.reminder_class.view_reminders()  # Fetch all reminders
            now = datetime.now().strftime("%Y-%m-%d %H:%M")
            for reminder in reminders:
                reminder_id, description, due_date = reminder
                if due_date == now:  # If the due date matches current time
                    print(f"Reminder Alert! '{description}' is due today at {due_date}.")
            time.sleep(60)  # Check every minute

    def start_scheduler(self):
        """Starts the scheduler in a separate thread."""
        thread = threading.Thread(target=self.reminder_scheduler)
        thread.daemon = True  # Ensures the thread exits when the main program exits
        thread.start()
