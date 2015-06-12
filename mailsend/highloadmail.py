#!/usr/bin/python3

import os

import smtplib

from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

loadout = os.getloadavg()  #this returns a tuple (0.34, 0.1, 0.07)

if loadout[1] > 0:

    msg = MIMEMultipart()  #msg is instance obj of mimemultipart

    msg['From'] = "nagios@localhost"  # this is seen as from: in receiving end

    msg['To'] = "sysadmin@gmail.com"  #put any thing here

    msg['Subject']="System load warning !!"

    body = str(loadout)

    msg.attach(MIMEText(body, 'plain'))

    fromaddr="pythoncheckload@localhost"    #returnpath

    toaddr="norbuurgen@gmail.com"    #actual receiving address

    server = smtplib.SMTP('localhost')

    server.set_debuglevel(True)  #for verbose output while testing

    text = msg.as_string()

    server.sendmail(fromaddr,toaddr,text)

   #server.sendmail(fromaddr,[toaddr],text)

    server.quit()
