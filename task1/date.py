import smtplib
from twilio.rest import Client
import datetime

# Set up email credentials
EMAIL_ADDRESS = 'your_email_address'
EMAIL_PASSWORD = 'your_email_password'

# Set up Twilio credentials
TWILIO_ACCOUNT_SID = 'your_twilio_account_sid'
TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'

# Define your friends and their birthdays/anniversaries
FRIENDS = {
    'Friend 1': {
        'birthday': '2023-05-01',
        'anniversary': '2023-07-15',
        'email': 'friend1@example.com',
        'phone': '+1234567890'
    },
    'Friend 2': {
        'birthday': '2023-08-12',
        'anniversary': '2023-06-20',
        'email': 'friend2@example.com',
        'phone': '+0987654321'
    }
}

# Function to send a birthday/anniversary message to a friend
def send_message(friend, message):
    if 'email' in friend:
        send_email(friend['email'], message)
    if 'phone' in friend:
        send_sms(friend['phone'], message)

# Function to send an email
def send_email(to, message):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_ADDRESS, to, message)

# Function to send an SMS message
def send_sms(to, message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        to=to,
        from_=TWILIO_PHONE_NUMBER,
        body=message)
    print(f'Sent message to {to}: {message.sid}')

# Get today's date
today = datetime.date.today()

# Check for birthdays and anniversaries
for friend, info in FRIENDS.items():
    if info['birthday']:
        bday = datetime.datetime.strptime(info['birthday'], '%Y-%m-%d').date()
        if bday.month == today.month and bday.day == today.day:
            message = f"Happy birthday, {friend}!"
            send_message(info, message)
    if info['anniversary']:
        anniversary = datetime.datetime.strptime(info['anniversary'], '%Y-%m-%d').date()
        if anniversary.month == today.month and anniversary.day == today.day:
            message = f"Happy anniversary
