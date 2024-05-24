mark21 = 45.5
mark11 = 45.5
mark13 = 45.5
mark41 = 45.5
mark16 = 45.5
mark32 = 45.5

 # same as array 

mark = [ 43.5, 534, 64, 434, 43.6]
print(type(mark), mark)
print(type(mark), mark[3]) # prints the value in 3rd place 
print(len(mark))



dhiren = [ "dhirendra" , 75 , "ktm"] # we can store multiple  types in python 
print(dhiren[0])
dhiren[0] = "clasher"
print(dhiren) # this works cause list are mutuable 


#slicing
dhirend = [45, 454, 54, 54, 3434, 5343, 534,]
dhirend [3:6]


str = "hello"
print(str[0])
str[0] = "y"   # this whole code block wont work cause strings  are unmutuable 