import math  # this is used to import multtiple maths signs ans snippets 

def circl(radui):  # function 
    print("hi")
    area = math.pi*radui**2 # this is get stored in the first variables if we have used multiple variables in to store data 
    circum2 = 2*math.pi * radui # this will store in the second variable cause of the hierarchy 
    return area, circum2

a, c = circl(4)  # here we have stored area and circumfrence of the numebr 4 ,this wass passed by user and it will now sote the values , 2 values in two variables and we can use them 
print("area:",a,"circi",c)


# this below program shows how we can reduce or print the number in an float value
value = 34.434343
formaed = "{:.2f}".format(value)
print(formaed)