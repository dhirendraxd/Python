with open("demo.txt", "r") as f:  # this simply means that now the file demo.txt can be accessed using f 
    #  data = f.read()
    #  print(data)
    # f.close  # we dont necessaraly need to close the file cause the use of with created close on it own using close wont make any errors btw...
    
    
with open("demo.txt","w") as f:
    f.write("newdata")