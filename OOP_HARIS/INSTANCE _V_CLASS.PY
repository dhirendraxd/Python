class employee:
    name = "dhiren" #this is an class attribute 
    lang = "eng"
    salary = 124232
    
harry = employee()
harry.name = "harish " #this is an object attribute 
print(harry.name, harry.lang)  #object attributes are give more priority then the class attribute