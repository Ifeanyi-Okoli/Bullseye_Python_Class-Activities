x = 1
# print(type("hello"))
# print(type(x))
# print(type([1,2,3]))
# print(type(("hello", "A", "B")))
# print(type({"hello", 1, 2, 3}))

string = "hello"
print(string.upper())

# def hello():
#     print("Hello")

# print(type(hello))

#mthod is a function that goes inside a class
class Dog:
    
    def __init__(self, name, age):
        self.name = name  #attribute of the class Dog, called name
        #self denotes the object
        self.age = age
        print(name)
        
    def get_name(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def setAge(self, age):
        self.age = age
      
    def bark(self):
        print("bark")

    def addOne(self, x):
        return x + 1
        
d = Dog("Tim", 30)  #instantiating a new instance of the class Dog
d.bark()  #calling the method bark inside the class Dog
Dog("Bill", 5).bark()  #the same as line 22
print(d.addOne(5)) # using print to display the value the method is returning
print(d.get_name())
print(d.getAge())
d.setAge(20)
print(d.getAge())



































