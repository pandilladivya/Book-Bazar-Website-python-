import smtplib
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import email.mime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#before running this application we should set the security by using following link
# https://www.google.com/settings/security/lesssecureapps
def emailms(taddr,msg):
    try:
        print("in the block ",taddr)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("kmitpython21@gmail.com","kmit@python21")
        msg1 = msg
        print(taddr)
        server.sendmail("kmitpython21@gmail.com",taddr, msg1)
        server.quit()
    except Exception as e:
        print(e)
