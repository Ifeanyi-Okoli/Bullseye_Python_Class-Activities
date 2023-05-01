# class Human:
#     breath = 
#     def __int__(height, name, complexion):
        


# maruche = Human (5.5, "Maruche", "black")

#mthods are used to alter the state of a class

# self referfs to the instance of the Class Car.

class Car:
    tyres = 4
    def __init__(self, model, type, brand, year, colour):
        self.model = model
        self.type = type
        self.brand = brand
        self.year = year
        self.colour = colour
        self.speed = 0
    
    def __str__(self) -> str:
        return f"Model: {self.model}, Type: {self.type}, Brand: {self.brand}, Year: {self.year}, Colour: {self.colour}"
    
    def run():
        pass
    
    def honk():
        pass
    
    def stop():
        pass
    
    def run(self):
        pass
    
    def run(cls):
        pass
    

v_boot = Car("E-300", "Benz", "Salon", "2003", "Blue")
camry = Car("Camry", "Toyota", "Salon", "2010", "Grey")

Car.tyres = 10

print(v_boot, camry)