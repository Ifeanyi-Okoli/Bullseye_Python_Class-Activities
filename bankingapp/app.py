"""Using OOP, implement a banking application that meets the following user requirements:
User can sign up / Register - 10 Marks
User can log in - 10 Marks.
User can deposit funds - 10 Marks.
User can Transfer Fund to another account - 10 Marks.
User can view Transaction History - 10 Marks.
User can check balance - 10 Marks.
Verbose Git commits - 10 Marks.
Comments and Docstrings - 10 Marks.
Code Readability - 10 Marks
Submission before deadline (Bonus) - 10 Marks.
You MAY use PayStack API to mock the transactions."""

import uuid
import datetime
from dataclasses import dataclass
from string import digits
import random


class User:
    history = dict()
    trasId = 0
    
    def __init__(self, name, email:str, password) ->None:
        self.id = uuid.uuid4().hex
        self.name = name
        self.email = email
        self.password = password
        self.balance = 0
        self.transaction = []
        
    def deposit(self, amount):
        self.balance += amount
        self.transaction.append({"amount": amount, "balance": self.balance, "time": datetime.datetime.now()})   
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction.append({"amount": -amount, "balance": self.balance, "time": datetime.datetime.now()})
        
    def transfer(self, amount, recipient):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction.append({"amount": -amount, "balance": self.balance, "time": datetime.datetime.now()})
            recipient.transaction.append({"amount": amount, "balance": recipient.balance, "time": datetime.datetime.now()})    
            return True
        else:
            return False
        
    def get_transaction_history(self):
        return self.transaction
    
    def get_balance(self):
        return self.balance
    
    def show_balance(self):
        print(f"Your balance is {self.balance}")
        
    def show_transaction(self):
        for transaction in self.transaction:
            amount = transaction["amount"]
            balance = transaction["balance"]
            time = transaction["time"]
            print(f"{time.strftime('%D')} \t {amount} \t {balance}")
            
        
class Bank:
    def __init__(self):
        self.users = []
        
    def register(self, name, email, password):
        for user in self.users:
            if user.email == email:
                print("Email already exists")
                return
        user = User(name, email, password)
        self.users.append(user)
        print("Registration Successful")
        return user
    
    def login(self, email, password):
        for user in self.users:
            if user.email == email and user.password == password:
                print("Login Successful")
                return user
        print("Invalid Credentials")
        return None
    

bank = Bank()

user1 = bank.register("John", "john.j@gmail.com", "pasword")

user1 = bank.login("john.j@gmail.com", "pasword")

user1.deposit(1000)

user2 = bank.register("Samuel", "samuel.a@gmail.com", "pasword")
user1.transfer(500, user2)

print(user1.get_transaction_history())
print(user1.get_balance())
