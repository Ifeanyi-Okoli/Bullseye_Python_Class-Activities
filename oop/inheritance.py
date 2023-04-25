class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age   
    def show(self):
         print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what I say")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)   #references the parent class 
        self.color = color
        # self.age = age

    def speak(self):
        print("Meow")

    def show(self):
         print(f"I am {self.name} and I am {self.age} years old, and I am {self.color}")


class Dog(Pet):
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

    def speak(self):
        print("Bark")


    


class Fish(Pet):
    pass

p = Pet("Tim", 19)
p.show()
c = Cat("Bill", 21, "White")
c.show()
d = Dog("Jill", 23)
f = Fish("Jim", 12)
c.speak()
d.speak()
f.speak()













