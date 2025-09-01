import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText

load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
USERNAME = "sadiqueiqbal28@gmail.com"
PASSWORD = os.getenv("APP_PSWD")
print(PASSWORD)

sender_email = "sadiqueiqbal28@gmail.com"
rec_email = "sadiqueotherstuff@gmail.com"
subject = "Test E-Mail from Python"
body = "Hello, This is a test email from Python"

message = MIMEText(body,"plain")
message["Subject"] = subject
message["From"] = sender_email
message["To"] = rec_email
print(message)

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.starttls()  # Secure the connection
    server.login(USERNAME, PASSWORD)  # Log in to SMTP server
    server.sendmail(sender_email, rec_email, message.as_string())  # Send email

print("Email sent successfully...!!")