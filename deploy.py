# https://github.com/ram133/picoclaw/deploy.py
# Path: picoclaw/deploy.py

import ftplib
import os

# CONFIGURATION
FTP_HOST = "132.148.223.185"
FTP_USER = "kgpmhwpltbje"
FTP_PASS = "biSB!N9rP@Ik"
LOCAL_DIR = os.path.expanduser("~/picoclaw")

def sync_to_web():
    """Autonomously syncs files to public_html/picoclaw/"""
    try:
        with ftplib.FTP(FTP_HOST) as ftp:
            ftp.login(user=FTP_USER, passwd=FTP_PASS)
            
            # Autonomously navigate to/create the production folder
            try:
                ftp.cwd('public_html/picoclaw')
            except:
                try:
                    ftp.cwd('public_html')
                    ftp.mkd('picoclaw')
                    ftp.cwd('picoclaw')
                except:
                    print("Action: CWD. Result: Using root directory.")

            for filename in os.listdir(LOCAL_DIR):
                path = os.path.join(LOCAL_DIR, filename)
                # Skip hidden files and directories
                if os.path.isfile(path) and not filename.startswith('.'):
                    with open(path, 'rb') as f:
                        ftp.storbinary(f"STOR {filename}", f)
            
        print("Action: Website Sync. Result: Files deployed to /public_html/picoclaw/.")
        return True
    except Exception as e:
        print(f"Action: Website Sync. Result: Failed. Error: {e}")
        return False

if __name__ == "__main__":
    sync_to_web()
