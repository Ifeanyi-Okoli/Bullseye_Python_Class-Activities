import pdb
import math

class Trigger:
    PI = math.pi
    
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def getRadius(self):
        return self.radius
    
    def area(cls):
        return cls.PI * (cls.getRadius**2)
    

circle1 = Trigger(7)
print(circle1.area())