# https://github.com/ram133/picoclaw/deploy.py
# Path: picoclaw/deploy.py

import ftplib
import os

# CONFIGURATION
FTP_HOST = "132.148.223.185"
FTP_USER = "kgpmhwpltbje"
FTP_PASS = "biSB!N9rP@Ik"
LOCAL_DIR = "/Users/cliffordhackett/picoclaw" # Standard path based on your terminal output

def sync_to_web():
    """Autonomously uploads repository files to the web server."""
    try:
        with ftplib.FTP(FTP_HOST) as ftp:
            ftp.login(user=FTP_USER, passwd=FTP_PASS)
            print("Action: FTP Login. Result: Success.")
            
            # Switch to public folder (usually public_html or similar)
            # ftp.cwd('public_html') 

            for filename in os.listdir(LOCAL_DIR):
                path = os.path.join(LOCAL_DIR, filename)
                if os.path.isfile(path) and not filename.startswith('.'):
                    with open(path, 'rb') as f:
                        ftp.storbinary(f"STOR {filename}", f)
                        print(f"Action: Sync {filename}. Result: Uploaded.")
        print("Result: Full Website Sync Complete.")
    except Exception as e:
        print(f"Result: Sync Failed. Error: {e}")

if __name__ == "__main__":
    sync_to_web()
