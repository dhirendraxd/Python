def factorial(n):
    # Base case: if n is 0, return 1
    if n == 0:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)

# Take input from the user
user_input = int(input("Enter a number to calculate its factorial: "))

# Call the factorial function with the user input and store the result in a variable
factorial_result = factorial(user_input)

# The result is stored in the 'factorial_result' variable
# You can use it for further processing or print it if needed
print(factorial_result)  # This line is optional and can be removed if you don't want to print the result
