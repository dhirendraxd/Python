from datetime import datetime
class Employee:
    name = "dhiren"  # This is a class attribute 
    lang = "eng"
    salary = 124232
    
    def getinfo(self):
        print(f"The lang is {self.lang}. Hey {self.salary}")
    
    @staticmethod
    def greet():
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Good morning. Current time is {current_time}")

harry = Employee()
harry.name = "harish"  # This is an instance or object  attribute is made for a individual  entity 
print(harry.name, harry.lang)

harry.getinfo()
harry.greet()