age = int(input("Enter your age: "))
print("Your age is:", age)

light = input("Enter the color of the light (red/green): ").lower()  # Convert the entered to lowerc case if user enter it in uppercase

if age >= 18 or light == "red":
    print("You can drive.")
elif age < 17 and light == "green":  
    print("You can't drive because your age is:", age)
else:
    print("Please enter a valid age and light color.")
   
# nested if else
if age>18: # first code executio and then it jumps to  another inside of it 
    if age>=80: # if this condition is true then it will print cannot drive in for then else will execute 
        print("you cannot drive ")
    else : print("you can drive")

else: print("cannot drive")