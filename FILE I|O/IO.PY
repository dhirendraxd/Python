filee = open("/home/dhiren/Documents/Codes/Python/FILE I|O/demo.txt", "r")  # r is used to read data form any files

data = filee.read()
data = filee.read(4)  #  this will now only read the first five characters inside that file

data = filee.readline()  # this will now read the first line only of the designated file and also provdies /n init wil give a space after the result is printed 

    # Read the next line
next_line = filee.readline() # this reads the next line we dont have to specifically speficy the line it works in hierarchy of the code written 
print(next_line)


  # Read the next 3rd line
    next_3line = filee.readline()
    print(next_3line)   # in this kind of case it will print an empty line totally blank 
    
    
print(data, type(data))  # prints the data inside the file and its types or the files stored data's type
filee.close
