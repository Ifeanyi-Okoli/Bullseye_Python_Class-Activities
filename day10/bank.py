from dataclasses import dataclass

@dataclass
class Customer:
    
    firstName = str()
    lastName = str()
    phoneNo = int()
    email = str()
    address = str()


@dataclass
class Bank:
    bankName = "Bank of America"
    
    def __init__(self) -> None:
        pass
    
    def __str__(self) -> str:
        return f"{self.bankName}"
    
    def deposit(self, amount):
        pass
    
    def withdrawal(self, amount):
        pass
    
    def viewHistory(self):
        pass
    
    def signUp(self):
        pass
    

wema = Bank()

customer1 = Customer("Coyeu", "Schaffer", ")