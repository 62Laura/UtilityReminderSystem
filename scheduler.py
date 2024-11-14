import time
import threading
from reminder import Reminder
from datetime import datetime

class ReminderScheduler:
    def _init_(self):
        self.reminder_class = Reminder  # Reference to the Reminder class

    def reminder_scheduler(self):
        while True:
            reminders = self.reminder_class.view_reminders()
            now = datetime.now().strftime("%Y-%m-%d %H:%M")
            for reminder in reminders:
                reminder_id, description, due_date = reminder
                if due_date == now:
                    print(f"Reminder Alert! '{description}' is due today at {due_date}.")
            time.sleep(60)

            def start_scheduler(self):
                thread = threading.Thread(target=self.reminder_scheduler)
                thread.daemon = True
                thread.start()