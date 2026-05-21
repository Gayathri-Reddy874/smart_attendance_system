import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from config import EMAIL_CONFIG


class EmailAlertSystem:
    def __init__(self):
        self.sender = EMAIL_CONFIG["sender"]
        self.password = EMAIL_CONFIG["password"]
        self.receiver = EMAIL_CONFIG["receiver"]

    def send_email(self, subject, body):
        msg = MIMEMultipart()
        msg["From"] = self.sender
        msg["To"] = self.receiver
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(self.sender, self.password)
        server.send_message(msg)
        server.quit()

    def attendance_alert(self, name):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        subject = f"Attendance Marked: {name}"
        body = f"Name: {name}\nTime: {now}\n\nAuto Alert"

        self.send_email(subject, body)