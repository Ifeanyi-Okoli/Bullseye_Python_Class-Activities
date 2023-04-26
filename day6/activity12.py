# Write an algorithm to generate a random password containing alphabeths, numbers, and special characters
import random
user = int(input("Please enter lenght of password: "))

def passwordGenerator(x):
    password = ""
    num = "1234567890"
    str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special = "~!@#$%^&*()"
    while len(password) <= x:
        password += random.choice(num)
        password += random.choice(str)
        password += random.choice(special)
    return password

print(passwordGenerator(user))