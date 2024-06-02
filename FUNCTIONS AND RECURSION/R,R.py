import math  # This imports the math module, which provides mathematical functions and constants.

# Function to calculate the area and circumference of a circle.
def circle(radius):
    print("hi")
    area = math.pi * radius**2  # Calculate the area of the circle.
    circumference = 2 * math.pi * radius  # Calculate the circumference of the circle.
    return area, circumference  # Return both values as a tuple.

# Call the function with radius 4 and unpack the returned tuple into variables 'a' and 'c'.
a, c = circle(4)
print("Area:", a, "Circumference:", c)  # Print the area and circumference.

# Demonstrate formatting a floating-point number to two decimal places.
value = 34.434343
formatted = "{:.2f}".format(value)  # Format 'value' to two decimal places.
print(formatted)  # Print the formatted value.


# Function to multiply two parameters.
def poli(p1, p2):  # Define a function named 'poli' that takes two parameters, p1 and p2.
    return p1 * p2  # Return the product of p1 and p2.

# Call the function 'poli' with 'd' and 2 as arguments and print the result.
print(poli('d', 2))  # Output: 'dd'

# Call the function 'poli' with 4 and 5 as arguments and print the result.
print(poli(4, 5))  # Output: 20


# Function to calculate the factorial of a number using recursion.
def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)

# Example usage:
print(factorial(5))  # Output: 120


# Function to calculate the nth Fibonacci number using recursion.
def fibonacci(n):
    # Base case: if n is 0, return 0; if n is 1, return 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: sum of the two preceding numbers
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage:
print(fibonacci(6))  # Output: 8


# Function to calculate the sum of digits of a number using recursion.
def sum_of_digits(n):
    # Base case: if n is a single digit, return n
    if n < 10:
        return n
    # Recursive case: sum the last digit and the sum of the remaining digits
    else:
        return n % 10 + sum_of_digits(n // 10)

# Example usage:
print(sum_of_digits(1234))  # Output: 10


# Function to reverse a string using recursion.
def reverse_string(s):
    # Base case: if the string is empty, return the empty string
    if len(s) == 0:
        return s
    # Recursive case: reverse the rest of the string and add the first character at the end
    else:
        return reverse_string(s[1:]) + s[0]

# Example usage:
print(reverse_string("hello"))  # Output: "olleh"


# Function to calculate the power of a number using recursion.
def power(base, exp):
    # Base case: any number to the power of 0 is 1
    if exp == 0:
        return 1
    # Recursive case: multiply the base by the result of the base raised to the exp-1
    else:
        return base * power(base, exp - 1)

# Example usage:
print(power(2, 3))  # Output: 8