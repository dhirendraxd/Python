def print_kwa(name, power):
    print("name", name, "power:", power)


# print_kwa(name = "dhiren", power = "laser")
print_kwa( power = "laser", name = "dhiren") #output : name dhiren power: laser  , order wont change 

# the positioning was beacasue it was a predefined program and so it  has fixed place in the function and i wont change even if we chnaged the postion 

# same program but user enters the input 
def print_kwa(name, power):
    print("name:", name, "power:", power)

# Take input from the user
name_input = input("Enter the name: ")
power_input = input("Enter the power: ")

# Call the function with the user inputs
print_kwa(name=name_input, power=power_input)
