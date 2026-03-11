# https://github.com/ram133/picoclaw/wp.py
# Path: picoclaw/wp.py

import smtplib
from email.message import EmailMessage

# CONFIGURATION
MY_EMAIL = "crh2509@icloud.com" 
MY_PASSWORD = "Crhrfrnr4$2" 
WP_TARGET = "Vewu327qaxi@post.wordpress.com"

def post(title, content):
    """Sends via verified iCloud account to bypass WP spam filters."""
    msg = EmailMessage()
    msg.set_content(f"{content}\n\n[end]") 
    msg['Subject'] = title
    msg['From'] = MY_EMAIL
    msg['To'] = WP_TARGET

    try:
        with smtplib.SMTP_SSL("smtp.mail.me.com", 465) as server:
            server.login(MY_EMAIL, MY_PASSWORD)
            server.send_message(msg)
        print("Action: WP post. Result: Success.")
        return True
    except Exception as e:
        print(f"Action: WP post. Result: Failed. Error: {e}")
        return False

if __name__ == "__main__":
    post("PicoClaw Test", "System check: wp.py is operational. [end]")
