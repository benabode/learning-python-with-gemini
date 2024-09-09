
# # Class dog: the blueprint for creating objects
# class Dog:
#     # Methods: Functions inside of classes
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
    
#     def bark(self):
#         print("Woof!")

# barny = Dog("Barny", "Leonberger")
# print(barny.name)
# barny.bark()


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def make_sound(self):
#         print("Generic sound")

# class Cat(Animal):
#     def make_sound(self):
#         print("Meow!")

# class Dog(Animal):
#     def make_sound(self):
#         print("Woof!")

# cat = Cat("Whiskers")
# dog = Dog("Barny")



# cat.make_sound()
# dog.make_sound()

#Task 1: Person Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("My name is " + self.name + " and I am ", self.age , "years old.")

personA = Person("Ben", 32)
personA.introduce()

#Task 2: Student subclass
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
        
    def introduce(self):
        print(f"Hello, I'm {self.name}, a student in grade {self.grade}.")

studentA = Student("Karl", "25", 12)
studentA.introduce()


#Task 3: Teacher subclass
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    def introduce(self):
        print(f"I'm teacher {self.name} and teach {self.subject} here.")

teacherA = Teacher("Mr.Stein", 30, "Computer Science")
teacherA.introduce()