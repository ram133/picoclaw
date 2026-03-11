# https://github.com/ram133/picoclaw/deploy.py
# Path: picoclaw/deploy.py

import ftplib
import os
from datetime import datetime
from wp import post

FTP_HOST = "132.148.223.185"
FTP_USER = "kgpmhwpltbje"
FTP_PASS = "biSB!N9rP@Ik"
LOCAL_DIR = os.path.expanduser("~/picoclaw")

def sync_to_web():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        with ftplib.FTP(FTP_HOST) as ftp:
            ftp.login(user=FTP_USER, passwd=FTP_PASS)
            try:
                ftp.cwd('public_html/picoclaw')
            except:
                ftp.cwd('public_html')
                ftp.mkd('picoclaw')
                ftp.cwd('picoclaw')

            for filename in os.listdir(LOCAL_DIR):
                path = os.path.join(LOCAL_DIR, filename)
                if os.path.isfile(path) and not filename.startswith('.'):
                    with open(path, 'rb') as f:
                        ftp.storbinary(f"STOR {filename}", f)
        
        # Write to local log
        with open("sync.log", "a") as log:
            log.write(f"[{timestamp}] SUCCESS: iMac synced to Website.\n")
        
        # Autonomous WP Heartbeat
        post("System Heartbeat: Sync Success", f"iMac automation completed sync at {timestamp}. All systems live.")
        print(f"Action: Deployment. Result: Success at {timestamp}.")
        
    except Exception as e:
        with open("sync.log", "a") as log:
            log.write(f"[{timestamp}] FAILED: {e}\n")
        post("System Alert: Sync Failed", f"Error during morning sync: {e}")

if __name__ == "__main__":
    sync_to_web()
