class Employee:
    """This is a class of employees for the company. It is the blueprint of the different employee objects that will be created."""
    #Class Variables
    companyName = "ABC Company"
    
    #constructor to initialize the object
    def __init__ (self, name, salary):
        #Instance variable
        self.name = name
        self.__salary = salary
    
    #Instance method
    def show(self):
        print("\n Employee:", self.name, "\n Salary: ", self.__salary, "\n Company: ", self.companyName)

#create first object        
empl1 = Employee("John Josiah", 100000)
empl1.show()

#create second object
empl2 = Employee("John Adegun", 150000)
empl2.show()

print(empl1.__salary)