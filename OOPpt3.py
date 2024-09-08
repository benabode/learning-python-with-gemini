from datetime import datetime

#Task 1 - Create person class

class Person:
    def __init__(self, name, age, city): #creation of attributes (variables) inside the class.
        self.name = name
        self.age = age
        self.city = city
    
    def introduce(self): #Method (function) that uses above attributes for a given purpose.
        current_year = datetime.now().year
        if self.name.startswith("S"):
            print(f"Hello user S, S as in {self.name}. Your where born on the year: ", current_year - self.age) 
        else:
            print(f"User {self.name} has entered with the age of {self.age}. User is from the city {self.city}")

# userA = Person("Ben", 32, "Stockholm")
# userB = Person("Sabrina", 33, "Stockholm")
# userA.introduce()
# userB.introduce()
#Task 2 - Create a Sub class of Person called Student with a additional attribute and ovveride the method
class Student(Person):
    def __init__(self, name, age, city, grade):
        super().__init__(name, age, city)
        self.grade = grade
    def introduce(self):
        print(f"My name is {self.name} and I'm a student in {self.city}. Currently I'm a student in the {self.grade} grade.")

# studentA = Student("Bert", 19, "Malmö", 13)
# studentA.introduce()

class Teacher(Person):
    def __init__(self, name, age, city, subject):
        super().__init__(name, age, city)
        self.subject = subject

    def introduce(self):
        add_title = "Mr." + self.name 
        print(f"My name is {add_title} and I'm a teacher in {self.city} lecturing in {self.subject}")

# teacherA = Teacher("Andre", 34, "Göteborg", "Art and History")
# teacherA.introduce()

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, deposit):
        self.balance += deposit
        print(f"Deposit successful. Your balance is: {self.balance}")
    
    def withdraw(self, withdrawl):
        if  withdrawl > self.balance:
            print(f"Insufficient balance. Current balance is: {self.balance} while withdrawl attempt is: {withdrawl}")
        else:
            self.balance -= withdrawl
            print(f"Withdrawn: {withdrawl}. You're current balance is: {self.balance}")

account = BankAccount(123456, 500)
account.deposit(500)
account.withdraw(700)
print(account.get_balance())