class Circle:
    pi = 3.142
    
    def __init__(self, radius):
        self.radius = radius
        
    def calculateArea(self):
        return Circle.pi * self.radius * self.radius
    
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def calculateArea(self):
        return self.length * self.width
    
#function
def area(shape):
    return shape.calculateArea()
    
#create object
cir = Circle(7)
rec = Rectangle(5, 6)

#call the common function

print(area(cir))
print(area(rec))