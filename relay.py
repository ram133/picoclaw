# https://github.com/ram133/picoclaw/relay.py
# Path: picoclaw/relay.py

import smtplib
from email.message import EmailMessage

# CONFIGURATION
# Use your actual Gmail/iCloud address and an App Password
MY_EMAIL = "yourname@gmail.com" 
MY_PASSWORD = "xxxx-xxxx-xxxx-xxxx" # Get this from Google/Apple Security settings
WP_TARGET = "Vewu327qaxi@post.wordpress.com"

def send_to_wp(title, content):
    """Sends via your actual account so WordPress trusts it."""
    msg = EmailMessage()
    msg.set_content(content)
    msg['Subject'] = title
    msg['From'] = MY_EMAIL
    msg['To'] = WP_TARGET

    try:
        # For Gmail: smtp.gmail.com | For iCloud: smtp.mail.me.com
        host = "smtp.gmail.com" if "gmail" in MY_EMAIL else "smtp.mail.me.com"
        
        with smtplib.SMTP_SSL(host, 465) as server:
            server.login(MY_EMAIL, MY_PASSWORD)
            server.send_message(msg)
        print("Action: Post sent. Result: WordPress should accept this as a verified sender.")
    except Exception as e:
        print(f"Action: Post failed. Result: {e}")

if __name__ == "__main__":
    # Test execution
    send_to_wp("Autonomous Realty Lead", "Price: $150k | ROI: 12% [end]")
