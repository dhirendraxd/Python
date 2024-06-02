def poli(p1, p2) :
    return p1*p2

print(poli('d',2))
print(poli(4,5))

#explainnation 

def poli(p1, p2):  # Define a function named 'poli' that takes two parameters, p1 and p2.
    return p1 * p2  # Return the product of p1 and p2.

# Call the function 'poli' with 'd' and 2 as arguments and print the result.
# In this case, since p1 is a string and p2 is an integer, it will repeat the string 'd' 2 times.
print(poli('d', 2))  # Output: 'dd'

# Call the function 'poli' with 4 and 5 as arguments and print the result.
# In this case, both p1 and p2 are integers, so it will return the product of 4 and 5.
print(poli(4, 5))  # Output: 20
