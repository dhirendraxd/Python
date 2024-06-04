username = "dhiren"
def func():
    # username = "cookies"
    print(username)
    
print(username)
func() # if we comment the username inside the function then it will print the username which is inside the function as :  print(username)  : this will not print the value outside of the funtion haveing the same variables name  result :dhiren
x = 43
def func2(y):
    z = x + y  # hence x is being used inside the function , which is basically decalared outside the function  will be used (its value will be used )
    return z

result = func2(1)

print(result) #output :44

yello = 99 # global variable 

def func3():

    global yello  #not used widely but 
      # global yello initialize the value of yello  to 980 cause we have used gloabl yello as refernce to assign a new value to yello variables 

    yello = 980

func3() # an function shoudl alwasy becalled before we use it or access any things inside it 


print(yello) #output 980 cause of the use of global yello used 

x2 = 876
def f1():
    # x2 = 48  # what if this is not availabe of isnt here 
    def f2():
        print(x2) # output 48: #if x2 isnt availbel inside the fuction then it will print the global vairable and it will print 876
    f2()
f1()

