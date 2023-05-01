class Vehicle:
    color = "white"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"    
    
    def show(self):
        print("Max speed:", self.max_speed)
        print("Mileage:", self.mileage)
        print(self.seating_capacity(50))

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, model, year):
        super().__init__(name, max_speed, mileage)
        self.model = model
        self.year = year
        
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

car = Vehicle("Toyota", 240, 18)

car.show()
print(car.seating_capacity(5))

bus = Bus("Toyota", 240, 18, "Corolla", 2010)
bus.show()
print(bus.seating_capacity())
print(isinstance(bus, Vehicle))
print(type(bus))
print(bus.color)