import sys
import os
import smtplib
from email.mime.text import MIMEText

def send_email(message):
    sender = os.environ.get('SMTP_SENDER')
    recipient = os.environ.get('SMTP_RECIPIENT')
    password = os.environ.get('SMTP_PASSWORD')
    subject = 'Message from Webpage'
    body = message

    if not sender or not recipient or not password:
        print('Sorry, messaging service is not configured.')
        return

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient


    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, password)
            server.sendmail(sender, recipient, msg.as_string())
        print('Message sent successfully. Thank you!')
    except Exception as e:
        print(f'Sorry, messaging service is currently down: {e}')

if __name__ == "__main__":
    message = sys.argv[1]
    send_email(message)
