from datetime import datetime

class Employee:
    # Class attributes
    name = "dhiren"
    lang = "eng"
    salary = 124232
    
    def __init__(self, name, lang, salary):
        # Instance attributes
        self.name = name
        self.lang = lang
        self.salary = salary
        print("I am passing an object")
    
    
    
    def getinfo(self):
        print(f"The lang is {self.lang}. Hey {self.salary}")
    
    @staticmethod
    def greet():
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Good morning. Current time is {current_time}")

# Creating an instance of Employee with the specified attributes
harry = Employee("hary", "eng", 42352)
print(harry.name, harry.lang)

harry.getinfo() #we dont print function and class

harry.greet()# we dont print class and functions
