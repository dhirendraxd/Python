# 1. For Loop
print("For Loop Example:")
for i in range(5):
    print(i)  # Output: 0 1 2 3 4

# 2. While Loop
print("\nWhile Loop Example:")
count = 0
while count < 5:
    print(count)
    count += 1  # Output: 0 1 2 3 4

# 3. Nested Loops
print("\nNested Loop Example:")
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
# Output:
# i=0, j=0
# i=0, j=1
# i=1, j=0
# i=1, j=1
# i=2, j=0
# i=2, j=1

# 4. Using break in Loops
print("\nUsing break in Loop Example:")
for i in range(10):
    if i == 5:
        break
    print(i)  # Output: 0 1 2 3 4

# 5. Using continue in Loops
print("\nUsing continue in Loop Example:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # Output: 1 3 5 7 9

# 6. Using else with Loops
print("\nUsing else with Loop Example:")
for i in range(5):
    print(i)
else:
    print("Loop completed without break")  # Output: 0 1 2 3 4 Loop completed without break

# 7. Infinite Loop with break
print("\nInfinite Loop with break Example:")
count = 0
while True:
    print(count)
    count += 1
    if count == 5:
        break  # Output: 0 1 2 3 4

# 8. The pass Statement
print("\nThe pass Statement Example:")
for i in range(5):
    if i == 3:
        pass  # Placeholder for future code
    else:
        print(i)  # Output: 0 1 2 4

# 9. Iterating over a List
print("\nIterating over a List Example:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Output: apple banana cherry

# 10. Iterating over a Dictionary
print("\nIterating over a Dictionary Example:")
person = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 25
# city: New York

# 11. Using enumerate()
print("\nUsing enumerate() Example:")
for index, value in enumerate(fruits):
    print(f"{index}: {value}")
# Output:
# 0: apple
# 1: banana
# 2: cherry

# 12. Using zip()
print("\nUsing zip() Example:")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
# Output:
# Alice is 25 years old
# Bob is 30 years old
# Charlie is 35 years old

# 13. List Comprehensions with Loops
print("\nList Comprehensions with Loops Example:")
squares = [x ** 2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# 14. Dictionary Comprehensions with Loops
print("\nDictionary Comprehensions with Loops Example:")
square_dict = {x: x ** 2 for x in range(5)}
print(square_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
