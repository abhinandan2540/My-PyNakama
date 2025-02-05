import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
load_dotenv()

# sender and reciever emails
sender_mail = os.getenv("SENDER")
reciever_mail = os.getenv("RECIEVER")
app_password = os.getenv("APP_PASSWORD")
msg = MIMEMultipart()
msg["Form"] = sender_mail
msg["To"] = reciever_mail
msg["Subject"] = "python email testing"
msg.attach(MIMEText("hello this is python mail testing 2"))

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_mail, app_password)
    server.sendmail(sender_mail, reciever_mail, msg.as_string())
    server.quit()
    print("mail send sucessfully")
except Exception as e:
    print(f"error : {e}")
