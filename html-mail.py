import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
USERNAME = os.getenv("LOGIN_USERNAME")
PASSWORD = os.getenv("APP_PSWD")

sender_email = input("Sender's Email: ")
reciever_email = input("Receiver's Email: ")
subject = "HTML body from Python"
html_body = """
<html>
  <body>
    <h2>Hello,</h2>
    <p>This is an <b>HTML</b> email sent using <a href="https://python.org">Python</a>.</p>
  </body>
</html>
"""

message = MIMEText(html_body,"html")
message["Subject"] = subject
message["From"] = sender_email
message["To"] = reciever_email

with smtplib.SMTP(SMTP_SERVER,SMTP_PORT) as server:
    server.starttls()
    server.login(USERNAME,PASSWORD)
    server.sendmail(sender_email,reciever_email,message.as_string())

    print(f"Email sent successfully to {reciever_email}")