import csv
import datetime
import smtplib
from twilio.rest import Client

class Friend:
    def __init__(self, name, email, phone, birthday, anniversary):
        self.name = name
        self.email = email
        self.phone = phone
        self.birthday = datetime.datetime.strptime(birthday, '%Y-%m-%d').date()
        self.anniversary = datetime.datetime.strptime(anniversary, '%Y-%m-%d').date()

class Reminder:
    def __init__(self, username, password, twilio_sid, twilio_token, twilio_phone):
        self.username = username
        self.password = password
        self.twilio_sid = twilio_sid
        self.twilio_token = twilio_token
        self.twilio_phone = twilio_phone
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend)

    def send_email(self, recipient, subject, message):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.username, self.password)
        server.sendmail(self.username, recipient, f'Subject: {subject}\n\n{message}')
        server.quit()

    def send_sms(self, recipient, message):
        client = Client(self.twilio_sid, self.twilio_token)
        message = client.messages.create(body=message, from_=self.twilio_phone, to=recipient)
        print(f"SMS sent to {recipient}. Message ID: {message.sid}")

    def send_reminder(self):
        today = datetime.date.today()
        for friend in self.friends:
            if today == friend.birthday:
                subject = f"Happy Birthday {friend.name}!"
                message = f"Dear {friend.name},\n\nWishing you a very happy birthday today!\n\nBest regards,\n[Your Name]"
                if friend.email:
                    self.send_email(friend.email, subject, message)
                if friend.phone:
                    self.send_sms(friend.phone, message)
            elif today == friend.anniversary:
                subject = f"Happy Anniversary {friend.name}!"
                message = f"Dear {friend.name},\n\nWishing you a very happy wedding anniversary today!\n\nBest regards,\n[Your Name]"
                if friend.email:
                    self.send_email(friend.email, subject, message)
                if friend.phone:
                    self.send_sms(friend.phone, message)

if __name__ == '__main__':
    reminder = Reminder('your_email@gmail.com', 'your_password', 'your_twilio_sid', 'your_twilio_token', 'your_twilio_phone_number')

    # Read friends data from a CSV file and create Friend objects
    with open('friends.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            friend = Friend(row['Name'], row['Email'], row['Phone'], row['Birthday'], row['Anniversary'])
            reminder.add_friend(friend)

    # Send reminders
    reminder.send_reminder()
