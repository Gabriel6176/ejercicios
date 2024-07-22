# Python email con attachment

from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from importlib.resources import contents
import smtplib
from email import message
import os

from_addr='gabriel.meijide@gmail.com'
to_addr='gabriel_meijide@hotmail.com'
subject='objeto'
body='texto del body'
msg = message.Message()
msg.add_header('from',from_addr)
msg.add_header('to',to_addr)
msg.add_header('subject',subject)
msg.set_payload(body)

'''
msg=MIMEMultipart()
msg['From']=from_addr
msg['To']=to_addr
msg['Subject']=subject
body=MIMEText(contents, 'plain')
msg.attach(body)

APP_PATH=os.getcwd()
filename=APP_PATH+'\\'+'test.txt'
with open (filename, 'r') as f:
    attachment=MIMEApplication(f read(), Name=basename(filename))
    attachment['Content-Disposition']='attachment; filename="{}"'.format(basename(filename))
msg.attach(attachment)
'''
server=smtplib.SMTP('smtp.gmail.com', 587)
server.login(from_addr, 'xxxx')

server.send_message(msg, from_addr=from_addr, to_addrs=[to_addr])

