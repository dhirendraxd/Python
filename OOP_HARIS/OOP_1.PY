# in this code  name is the attribute and salary ans langa are class  attributes as they belong to the class 

class employee:
    name = "dhiren" #this is an class attribute 
    lang = "eng"
    salary = 124232
    
harry = employee()
harry.name = "harish " #this is an object attribute 
print(harry.name, harry.lang)

rohan = employee()
rohan.name= "rohit"
print(rohan.salary, rohan.lang,rohan.name)
