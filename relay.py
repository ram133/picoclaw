# /Users/Shared/relay.py

import smtplib
from email.message import EmailMessage

def send_relay_email(service, recipient, subject, body):
    # Configuration for Gmail and iCloud
    configs = {
        "gmail": {"host": "smtp.gmail.com", "port": 587, "user": "YOUR_GMAIL@gmail.com"},
        "icloud": {"host": "smtp.mail.me.com", "port": 587, "user": "YOUR_ICLOUD@icloud.com"}
    }
    
    # Universal password provided by user
    pw = "Crhrfrnr4$2"
    
    conf = configs.get(service.lower())
    if not conf:
        print("Invalid service choice.")
        return

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = conf['user']
    msg['To'] = recipient

    try:
        with smtplib.SMTP(conf['host'], conf['port']) as server:
            server.starttls()
            server.login(conf['user'], pw)
            server.send_message(msg)
            print(f"Successfully sent via {service}")
    except Exception as e:
        print(f"Failed to send: {e}")

# Example usage for realty.py integration:
# send_relay_email("gmail", "lead_target@email.com", "New Lead!", "Details here...")
