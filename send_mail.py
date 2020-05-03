import smtplib
from email.mime.text import MIMEText


def sendmail():
    gmail_user = 'YOUR ACCOUNT'
    gmail_password = 'YOUR PWD'

    msg = MIMEText('Item Restock')
    msg['Subject'] = 'Test'
    msg['From'] = gmail_user
    msg['To'] = 'RECEIVER ACCOUNT'

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.send_message(msg)
    server.close()

    print('Email sent!')
