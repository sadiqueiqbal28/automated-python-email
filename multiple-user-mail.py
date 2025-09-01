import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText

load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
USERNAME = os.getenv("LOGIN_USERNAME")
PASSWORD = os.getenv("APP_PSWD")

count = 1
lor = [] # List of receipient
num = int(input("Number of people to send the mail: "))

sender_email = input("Sender's Email: ")

while (count <= num):
    reciever_email = input(f"Enter {count} mail reciepient: ")
    lor.append(reciever_email)
    count += 1

sub = "This is a system generated mail sent by Sadique Iqbal"
html_body = """
<html>
    <body>
        <h2>Mail by Sadique Iqbal</h2>
        <p>This mail was sent by Sadique Iqbal while testing automated mail using Python</p>
    </body>
</html>
"""

message = MIMEText(html_body,"html")
message["Subject"] = sub
message["From"] = sender_email
message["To"] = ", ".join(lor)

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.starttls()
    server.login(USERNAME, PASSWORD)
    for rec in lor:
        server.sendmail(sender_email, rec, message.as_string())
        print(f"Email has been sent successfully to {rec}")