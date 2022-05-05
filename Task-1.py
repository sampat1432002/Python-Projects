import smtplib
from email.message import EmailMessage


def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "sampat1432002@gmail.com"
    msg['from'] = user
    password = "eqfjqpkokrugfuwk"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

try:
    email_alert("Daily Attendance", "Hi", "190390107027@saffrony.ac.in")
    print("Success")
except:
    print("failure")