# https://github.com/ram133/picoclaw/wp_mailer.py
# Path: picoclaw/wp_mailer.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# CONFIGURATION - MUST MATCH YOUR WORDPRESS ACCOUNT EMAIL
SENDER_EMAIL = "your-account-email@gmail.com" 
SENDER_PASSWORD = "your-app-password" # Use a Google App Password, not your login password
WP_POST_EMAIL = "Vewu327qaxi@post.wordpress.com"

def send_to_wordpress(subject, body):
    """
    Autonomously sends content to WordPress via Post-by-Email.
    The 'subject' becomes the Post Title.
    """
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = WP_POST_EMAIL
    msg['Subject'] = subject

    # WordPress prefers simple HTML or Plain Text
    msg.attach(MIMEText(body, 'html'))

    try:
        # Using Gmail SMTP settings (Standard/Free)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, WP_POST_EMAIL, msg.as_string())
        print(f"SUCCESS: Post '{subject}' sent to WordPress.")
        return True
    except Exception as e:
        print(f"FAILED: Could not send post. Error: {e}")
        return False

if __name__ == "__main__":
    # Test Post
    test_title = "Automated Realty Lead Test"
    test_body = "<h1>New Lead Found</h1><p>This is an autonomous test from PicoClaw.</p>"
    send_to_wordpress(test_title, test_body)
