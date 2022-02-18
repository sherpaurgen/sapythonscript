#!/usr/bin/env python3
# usage:
# python /path/to/testSmtp.py
import smtplib,ssl,getpass,time
try:
    smtpServer=input("Enter smtp server ip: ")
    smtpPort=input("Enter TLS port(eg. 587): ")
    sender = input("Enter From addr: ")
    secret=getpass.getpass()
    receiver = input("Enter To addr: ")
    context=ssl.create_default_context()
    server = smtplib.SMTP(smtpServer,smtpPort)
    server.starttls(context=context)
    time.sleep(1)
    server.ehlo()
    time.sleep(1)
    server.login(sender, secret)
    #https://datatracker.ietf.org/doc/html/rfc822.html#section-3.1.2
    message=("Subject: SMTP test\r\n")
    message=message+"\r\nThis is smtp test message\r\n"  
    time.sleep(1) 
    server.sendmail(sender, receiver, message)
    server.quit()
    print("Mail sent..")

except Exception as e:
    print(e)
finally:
    server.close       
