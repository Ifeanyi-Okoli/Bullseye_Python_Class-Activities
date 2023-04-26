# Write a python script that will automatically send an email or SMS (or both) to your Friends on their birthday and wedding Anniversary.
import datetime
import smtplib
# import requests
import os
import random
import csv
import email
import ssl
# import Client from twilio
from twilio.rest import Client

#List of friends with their details
friendsList = {
    "Jacob": {"birthday": "25-04-1980", "anniversary": "30-04-2010", "phone": "1234567890", "email": "john.josiah@gmail.com"},
    "Richard": {"birthday": "26-04-1980", "anniversary": "29-04-2010", "phone": "08035138223", "email": "richard.james@gmail.com"},
    "Simon": {"birthday": "27-04-1980", "anniversary": "28-04-2010", "phone": "0178593456", "email": "simon.michael@gmail.com"},
    "Peter": {"birthday": "01-05-1980", "anniversary": "02-05-2010", "phone": "1234567890", "email": "peter.drucker@gmail.com"},
        }
               
# Email Account Details
myEmail = "fnykly@gmail.com"
myPassword = "Amanda*2020"               
               
# Server Details
smtpServer = "smtp.gmail.com"
smtpPort = 465                
context= ssl.create_default_context()     
#Function to send email
def sendEmail(subject, message, to_email):
    with smtplib.SMTP(smtpServer, smtpPort, context) as smtp:
        smtp.starttls()
        smtp.login(myEmail, myPassword)
        smtp.sendmail(myEmail, to_email, f"Subject: {subject}\n\n{message}")
               
               
#todays date
today = datetime.date.today()

for friend, details in friendsList.items():
    #Check if today is friend's birthday
    bday = datetime.datetime.strptime(details["birthday"], '%d-%m-%Y').date()
    if today.month == bday.month and today.day == bday.day:
        # Send birthday email
        subject = f"Happy Birthday {friend}!"
        message = f"Dear {friend},\n\nWishing you a very happy birthday! Have a wonderful day.\n\nBest Regards,\nIfeanyi Okoli"
        to_email = details["email"]
        sendEmail(subject, message, to_email)
        print(message)
               
    #Check if today is friend's anniversary
    anniv = datetime.datetime.strptime(details["anniversary"], '%d-%m-%Y').date()
    if today.month == anniv.month and today.day == anniv.day:
        # Send anniversary email
        subject = f"Happy Anniversary {friend}!"
        message = f"Dear {friend},\n\nWishing you a very happy wedding anniversary! May your love continue to grow stronger with each passing year.\n\nBest Regards,\nIfeanyi Okoli"
        to_email = details["email"]
        sendEmail(subject, message, to_email)    
        print(message)           
               
               
               
               
               
               

# date_str = today.strftime("%d/%m/%Y")
# print("Today's date is:", date_str)






account_sid = 'ACeefa90de72fe4002b92f11a7eff42f1e'
auth_token = '768cc172bd353ee747969e53e07108f7'
client = Client(account_sid, auth_token)




message = client.messages.create(
    to='+2347062021434',
    from_='+1 607 400 8018',
    body='Hello from Python!'
)

print(message.sid)