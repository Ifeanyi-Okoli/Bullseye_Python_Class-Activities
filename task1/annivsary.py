# Write a python script that will automatically send an email or SMS (or both) to your Friends on their birthday and wedding Anniversary.
import datetime
import smtplib
import csv

class Friends:
    
    def __init__(self, name, email, phone, birthday, anniversary):
        self.name = name
        self.email = email
        self.phone = phone
        self.birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()
        self.anniversary = datetime.datetime.strptime(anniversary, "%Y-%m-%d").date()