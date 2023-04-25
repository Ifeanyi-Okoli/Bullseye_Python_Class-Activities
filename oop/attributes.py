#8 Class attributes are attributes that are specifi to the clas and not an instance of the clas or object of the class

#Classes are exportable
class Person:
    number_of_people = 0 #this is specific to the class. This means it does not change with the different instances.
    
    def __init__(self, name):
        self.name = name
        Person.add_person()
        # Person.number_of_people += 1
  #Class methods acts on the class itself. It is identified with teh @classmerthod before the method declaration 
  #It uses cls insteadof self   
  #class method does not =reference self or instance of a class, but they reference the class itself.  
    @classmethod
    def number_of_people(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1
    
    
p1 = Person("Jim")
p2 = Person("Tim")
print(p2.number_of_people)
Person.number_of_people = 8
print(p2.number_of_people)





















