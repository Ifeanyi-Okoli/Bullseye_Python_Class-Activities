class Student:
    def __init__(self, name, age, level, gender):
        self.name = name
        self.age = age
        self.level = level
        self.gender = gender
        
    def __str__(self):
        return self.name
    
    def __repr__(self) -> str:
        return f"Student(name={self.name}, age={self.age}, gender={self.gender})"
    
    def __eq__(self, o: object) -> bool:
        pass
    
stud1= Student("Gbenga Olaole", 32, 400, "female")

print(str(stud1))

print(repr(stud1))