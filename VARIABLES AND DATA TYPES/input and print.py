# print("enter your name ")
input("enter your name ")
# the input take user input form the input function   and displays it  afterwards 
print("hi ,user")

name=input("enter your id  ")
print("welcome ",name)

val=input("enter some value") #input always converts the input  to string 
print(type(val),val) # this will print  the type of the value in this case it will be str and its real value  as 43 entered 

numval=int(input("enter any integer num;"))  # we can take integer value form user by using int as shown in this code block 
print(type(numval),numval) # it will print the type of the enterd values whihc in thsi case will be int and enterd value will be printed 

age=int(input("enter your age"))
name=input("enter your name")
marks=float(input("enter your marks"))
# the above will conver the user input to their respective type if not then all of them will be considered as strings so it is necessary to define their type while taking user input 
print("your name is :",name)
print("your age is :",age)
print("yours marks are:",marks)