# 1. Defining and Calling a Simple Function
def greet():
    print("Hello, World!")

greet()  # Calling the function

# 2. Function with Parameters
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# 3. Function with Return Value
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8

# 4. Default Parameters
def greet(name="World"):
    print(f"Hello, {name}!")

greet()

# 5. Keyword Arguments
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet(pet_name="Willie")

# 6. Variable-Length Arguments (*args)
def make_pizza(*toppings):
    print("Making a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza("pepperoni", "mushrooms", "green peppers", "extra cheese")

# 7. Variable-Length Keyword Arguments (**kwargs)
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

# 8. Lambda Functions
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

# 9. Higher-Order Functions
def apply_function(func, value):
    return func(value)

double = lambda x: x * 2
print(apply_function(double, 5))  # Output: 10

# 10. Recursive Function
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# 11. Nested Functions
def outer_function(text):
    def inner_function():
        print(text)
    inner_function()

outer_function("Hello from the outer function!")

# 12. Closures
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier_of(3)
print(times3(9))  # Output: 27

# 13. Decorators
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
