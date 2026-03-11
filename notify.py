# https://github.com/ram133/picoclaw/notify.py
# Path: picoclaw/notify.py

import time
from wp import post

PROSPECT_FILE = "prospects.txt" # Monitored via the 9:00 AM sync

def check_new_leads():
    """Reads the latest entry from the root prospect list and alerts the user."""
    try:
        with open(PROSPECT_FILE, "r") as f:
            lines = f.readlines()
            if not lines:
                return
            
            last_lead = lines[-1].strip()
            # Prevent duplicate alerts by tracking the last alerted lead in sync.log
            with open("sync.log", "r") as log:
                if last_lead in log.read():
                    return

            # Action: Push to WordPress
            post("New B2B Lead Captured", f"New prospect details: {last_lead}")
            
            # Action: Log the alert
            with open("sync.log", "a") as log:
                log.write(f"Alerted: {last_lead}\n")
                
            print(f"Action: Mobile Notification. Result: Success for {last_lead}")
    except FileNotFoundError:
        print("Action: Lead Check. Result: prospects.txt not found yet.")

if __name__ == "__main__":
    check_new_leads()
