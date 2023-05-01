class Vehicle:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def drive(self):
        print("Driving", self.name, self.color, "vehicle")

    def turn(self, direction):
        print("Turning", self.name, "vehicle", direction)

    def brake(self):
        print(self.name, "vehicle is stopping")
    
    def info(self):
        print("Name:", self.name)
        print("Color:", self.color)
        print("Price:", self.price)
        
class Car(Vehicle):
    def __init__(self, name, color, price, manufacturer):
        super().__init__(name, color, price)
        self.manufacturer = manufacturer
        
    def drive(self):
        print("Driving", self.name, self.color, "car")
        
    def turn(self, direction):
        print("Turning", self.name, "car", direction)
        
    def brake(self):
        print(self.name, "car is stopping")
    
    def changeGear(self, gearName):
        print(self.name, "car is changing gear to", gearName)

car = Car("Corolla", "White", 100000, "Toyota")
car.brake()
car.turn("left")
car.changeGear("D")