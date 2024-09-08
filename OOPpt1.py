#Parent class (base class)
class Person:
    def __init__(self, name, age, city): #initialize attributes (variable) when creating "Person"
        self.name = name
        self.age = age
        self.city = city
    
    def introduce(self): #Method (function) to use attributes
        print(f"Hello, my name is {self.name} and I'm {self.age} old, living in {self.city}")

personA = Person("Ben", 32, "Gothenburg") #assign value to attributes (variables) inside of the class.
personA.introduce()

#Class inherits base info of person class with additional attribute (variable) of grade
class Student(Person):
    def __init__(self, name, age, city, grade):
        super().__init__(name, age, city)
        self.grade = grade
    
    def introduce(self):
        print(f"My name is {self.name}, and I'm a student in grade {self.grade}")

studentA = Student("Dennis", 24, "Stockholm", 12)
studentA.introduce()