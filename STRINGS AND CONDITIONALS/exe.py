name=input("enter your name ")
print(len(name),name)

dolla=input("input as many dolla sign as you cna ")
print("the values entered is :",dolla)
print("the dolla amount are ",dolla.count("$"))

marks=int(input("enter your marks "))

if marks>=90 : 
    print("your grade ia A")
elif marks>=80 and marks<90:
    print("the grade is B ")
elif marks>=70 and marks<80:
    print("the grade is C")
else :
    print("D ")
 
 
 num=int(input("enter an number"))
 
if num % 2==0 :
    print( "the numebr entered by user is odd")

else :
    prin("the numerb is even ")
    
enter="enter an number "
num1=int(input(enter))
num2=int(input(enter))
num3=int(input(enter))

if num1>num2  or num1>num3:
    print("num 1 is greater ")
elif num2>num3 :
    print("num 2 is greatr ")
else : print("num3 is greatr ")

#checke the multpile of  7 or not 

multip=int(input(enter))
if multip % 7==0:
    print("its devisible")

else: print("its not divisible")