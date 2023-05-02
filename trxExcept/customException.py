class NegativeAgeError(Exception):
    
    def __init__(self, age, ):
        message = f"Age cannot be negative, you entered {age}"
        self.age = age
        self.message = message
    
    age = int(input("Enter age: "))
    if age < 0:
        raise NegativeAgeError(age)