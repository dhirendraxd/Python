filee = open("/home/dhiren/Documents/Codes/Python/FILE I|O/demo.txt", "r") #r is used to read data form any files 

data = filee.read()
print(data, type(data))
filee.close
