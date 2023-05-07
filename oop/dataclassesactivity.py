from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    gender: str
    
    def __str__(self) -> str: #optional. It is used to print the object
        return f"Person(name={self.name}, age={self.age})"

person1 = Person("Adamu Ciroma", 23, "male")
print(person1)
print(person1.name)
print(type(person1))
# print(str(person1)) #needed when we are using __str__ method to print the object