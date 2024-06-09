with open("/home/dhiren/Documents/Codes/Python/MODULess/sample.txt", "r") as hey:
    data = hey.read()

newdata =  data.replace("java", "python")
print(newdata)
    
with open("/home/dhiren/Documents/Codes/Python/MODULess/sample.txt", "w") as hey:
    hey.write(newdata)
    