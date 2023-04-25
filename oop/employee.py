class Employee:
    
#    pass
# emp_1 = Employee()
# emp_2 = Employee()

# print(emp_1)
# print(emp_2)

# emp_1.first = "Coyeu"
# emp_1.last = "Schaffer"
# emp_1.email = "Coyeu.Schaffer@company.com"
# emp_1.pay = 50000

# emp_2.first = "Thomas"
# emp_2.last = "Schaffer"
# emp_2.email = "Thomas.Schaffer@company.com"
# emp_2.pay = 40000

# print(emp_1.email)
# print(emp_2.email)
    numOfEmps = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = (f"{first}.{last}@company.com")
        Employee.numOfEmps += 1
    
    def fullname(self):
        return f"{self.first} {self.last}"

    def applyRaise(self):
        self.pay = int(self.pay * 1.04)

#Class variables are shared by all instances of a class and are the same for all instances


emp_1 = Employee("Corey", "Schaffer", 60000)
emp_2 = Employee("Thomas", "Schaffer", 40000)

print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())
emp_1.applyRaise()
print(emp_1.pay)

print(emp_1.__dict__)  # used to access the name space of an instance of a class

print(Employee.numOfEmps)