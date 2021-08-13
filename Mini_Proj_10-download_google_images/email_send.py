import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from download_imgs import *
from grayscale import *
from resize import *
from zip_create import *
email_user='sendzip3@gmail.com'
email_send=input('Input Email Id to send the files to')

subject = 'Zipped files after grayscaling and resising'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject
body='Hi there, sending this email from Python to send the grayscale and resized images from google.'

msg.attach(MIMEText(body,'plain'))

#filename='resized_dir_zip.zip'
attachment  =open(filename+'.zip','rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename+'.zip')

msg.attach(part)
text = msg.as_string()



server=smtplib.SMTP('smtp.gmail.com',587) #gmail server and port number
server.starttls()#secure connections
server.login(email_user,'your_password_here')


server.sendmail(email_user,email_send,text)
server.quit()
