from dataclasses import dataclass
from string import digits
from datetime import datetime
import random


class Customer:
    
    history = dict()
    trans_id = 0
    
    def __init__(self, firstName:str, lastName:str, phoneNo:int, email:str, address:str, balance=0) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNo = phoneNo
        self.email = email
        self.address = address
        self.__balance = balance
        self.transaction = []
        
    def __str__(self) -> str:
        fullName = f"{self.firstName} {self.lastName}"
        fullName = lambda first, last: first + " " + last
        return f"{fullName(self.firstName, self.lastName)} \t {self.phoneNo} \t {self.email} \t {self.address} \t {self.balance}"
    
    def updateBalance(self, type, amount):
        """Updates the balance for deposit or credit transactions"""
        if type == "deposit":
            self.__balance += amount
        elif type == "withdrawal":
            if self.__balance <= amount:
                print("Insufficient funds")
                raise ValueError("Insufficient funds")
            else:
                self.__balance -= amount
        else:            
            print("Invalid transaction type")
            return
        
        self.transaction.append({"type": type, "amount": amount, "balance": self.__balance, "time": datetime.now()})
    
    @classmethod
    def updateHistory(cls, date, type, amount):
        """pdates the transaction history of the customer"""
        numbers = random.choices(digits, k=10)
        cls.__setattr__("account_number", numbers)
        cls.history[f"{date}"] = {"type": type, "amount": amount, "balance": cls.balance}
    
    @property
    def getBalance(self):
        return self.__balance
    
    def viewHistory(self):
        """Displays the transaction history of a customer"""
        history = ""
        for transadate, details in self.history.items():
            history += f"{transadate} \t {details['type']} \t {details['amount']} \t {details['balance']}\n"
        print(history)
        return history
    
    def generateAccount(self):
        """Generates an account number for a customer"""
        numbers = random.choices(digits, k=10)
        self.__setattr__("account_number", "".join(numbers))
        return self.account_number

@dataclass
class Bank:
    bankName = "Bank of America"
    
    customers = {}
    
    def deposit(self, account, amount):
        """Credits a customer's account"""
        customer = customer[account]
        customer.updateBalance("deposit", amount)
    
    def withdrawal(self, account, amount):
        """Debits a customer's account"""
        customer = self.customers[account]
        customer.updateBalance("withdrawal", amount)
    
    def viewHistory(self, account):
        """Displays the transaction history of a customer"""
        customer = self.customers[account]
        customer.viewHistory()
    
    def signUp(cls, firstName, lastName, phoneNo, email, address):
        """signs a new customer"""
        customer = Customer(firstName, lastName, phoneNo, email, address)
        accountNumber = customer.generateAccount()
        cls.customers[f'{accountNumber}'] = customer
        return customer
        

wema = Bank()

customer1 = Customer("Coyeu", "Schaffer", "09035138223", "maruche@gmail.com", "Lagos")
print(customer1.__dict__.items())

chima = wema.signUp("Chima", "Okeke", "09035138223", "chima@gmail.com", "Lagos")
chima.updateBalance("deposit", 1000)
chima.updateBalance("withdrawal", 500)
chima.updateBalance("deposit", 1000)

print(chima.getBalance)
#==============================================Inheritance


class Investors(Customer):
    
    def __init__(self, firstName, lastName, phoneNo, email, address, balance=0, investment=0) -> None:
        super().__init__(firstName, lastName, phoneNo, email, address, balance)
        self.investment = investment
        
    def loan(self):
        pass
    
    def fixed(self, amount, duration = 364, rate = 0.2):
        pass
    
    def birthday(self):
        pass
    
    

print(Investors.__dict__.items()) #prints all the attributes of the class
print(dir(Investors)) #prints all the attributes of the class
print("===============")
print(dir(Customer))