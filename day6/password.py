from string import digits, ascii_letters, punctuation
import random

# password = ""

def generatePassword(length):
    password = ""
    while len(password) < length:
        password += random.choice(digits)