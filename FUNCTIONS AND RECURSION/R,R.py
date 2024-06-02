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

