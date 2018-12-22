# coding=utf-8
'some comment...'
from email.mime.multipart import MIMEMultipart

__author__ = 'Jiateng Liang'

import smtplib
from email.mime.text import MIMEText
from bootstrap_init import app


def send_mail(title, content, emails=[]):
    msg = MIMEMultipart()
    username = app.config.get('EMAIL_USERNAME')
    password = app.config.get('EMAIL_PASSWORD')
    msg['From'] = username
    msg['To'] = ';'.join(emails)
    msg['Subject'] = title
    txt = MIMEText(content)
    msg.attach(txt)
    smtp = smtplib.SMTP()
    smtp.connect(app.config.get('EMAIL_SERVER'), app.config.get('EMAIL_PORT'))
    smtp.login(username, password)
    smtp.sendmail(username, emails, msg.as_string())
    smtp.quit()

