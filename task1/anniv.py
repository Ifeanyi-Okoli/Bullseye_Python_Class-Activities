import smtplib
import datetime
import random
import requests

# List of friends with their birthdays and wedding anniversaries
friends = {
    "John": {"birthday": "1980-03-15", "anniversary": "2010-05-20"},
    "Jane": {"birthday": "1990-04-25", "anniversary": "2015-06-10"},
    # Add more friends with their details
}

# Email account details
EMAIL_ADDRESS = "your_email_address_here"
EMAIL_PASSWORD = "your_email_password_here"

# SMTP server details
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Function to send email
def send_email(subject, message, to_email):
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_ADDRESS, to_email, f"Subject: {subject}\n\n{message}")

# Today's date
today = datetime.date.today()

for friend, details in friends.items():
    # Check if today is friend's birthday
    bday = datetime.datetime.strptime(details["birthday"], '%Y-%m-%d').date()
    if today.month == bday.month and today.day == bday.day:
        # Send birthday email
        subject = f"Happy Birthday {friend}!"
        message = f"Dear {friend},\n\nWishing you a very happy birthday! Have a wonderful day.\n\nBest Regards,\nYour Name"
        to_email = "friend_email_address_here"
        send_email(subject, message, to_email)

    # Check if today is friend's anniversary
    anniv = datetime.datetime.strptime(details["anniversary"], '%Y-%m-%d').date()
    if today.month == anniv.month and today.day == anniv.day:
        # Send anniversary email
        subject = f"Happy Anniversary {friend}!"
        message = f"Dear {friend},\n\nWishing you a very happy wedding anniversary! May your love continue to grow stronger with each passing year.\n\nBest Regards,\nYour Name"
        to_email = "friend_email_address_here"
        send_email(subject, message, to_email)
