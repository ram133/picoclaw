import smtplib
from email.message import EmailMessage

def send_relay_email(service, recipient, subject, body):
    # Fully configured for 3659745@gmail.com and crh2509@icloud.com
    configs = {
        "gmail": {
            "host": "smtp.gmail.com", 
            "port": 587, 
            "user": "3659745@gmail.com"
        },
        "icloud": {
            "host": "smtp.mail.me.com", 
            "port": 587, 
            "user": "crh2509@icloud.com"
        }
    }
    
    # Universal password: Crhrfrnr4$2
    pw = "Crhrfrnr4$2"
    
    conf = configs.get(service.lower())
    if not conf:
        print(f"Error: {service} is not a configured service.")
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
        print(f"Failed to send via {service}: {e}")

# Ready for integration with realty.py
