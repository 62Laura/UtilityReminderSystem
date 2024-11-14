import time
import threading
from reminder import view_reminders
from datetime import datetime

# Check reminders everyday
def reminder_scheduler():
    while True:
        reminders = view_reminders()
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        for reminder in reminders:
            reminder_id, description, due_date = reminder
            if due_date == now:
                print(f"Reminder Alert! {description} is due today.")
        time.sleep(86400)