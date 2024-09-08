#This exercise was to complicated as of now (8/09/2024). Asked Gemini to provide more exercises (OOPpt3)

class Shape:
    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    

        
def calculate_total_area(shapes):
    total_area = 0
    for shape in shapes:
        total_area += shape.calculate_area()
    return total_area

circle = Circle(5)
rectangle = Rectangle(4, 3)

shapes = [circle, rectangle]
total_area = calculate_total_area(shapes)
print("Total area:", total_area)