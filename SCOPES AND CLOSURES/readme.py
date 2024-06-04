# an function shoudl alwasy becalled before we use it or access any things inside it


def add_numbers(x, y):
  """Adds two numbers and returns the sum."""
  return x + y

# This will cause an error because the function hasn't been called yet
# and there's no value assigned to result
# result = add_numbers(5, 3)  # This line would cause an error

# Call the function to get the sum
result = add_numbers(5, 3)

print(result)  # Now this will print 8 (5 + 3)
