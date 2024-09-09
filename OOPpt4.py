import math

#Base class for all shapes. The abstract method seemed unnecessary to me at first but gemini explained that it was a "good practice to have", to ensure the method is used by all subclasses.
class Shape:
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius * self.radius
    
class Rectangle(Shape):
    def __init__(self, length, height):
        super().__init__()
        self.length = length
        self.height = height
    
    def calculate_area(self):
        return self.length * self.height
    
circle = Circle(5)
print("The area of the circle is: ", circle.calculate_area())

rectangle = Rectangle(4,3)
print("The are of the rectangle is: ", rectangle.calculate_area())

    