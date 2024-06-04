def ghar(num):
    def actual(x):
        return x ** num
    return actual

f = ghar(2)  # f is now a function that squares its input
g = ghar(3)  # g is now a function that cubes its input

print(f(3))  # Output: 9 (3^2)
print(g(4))  # Output: 64 (4^3)

# desctiption
# Create f by calling ghar(2):

# When ghar(2) is called, it returns a new function actual where num is set to 2.
# So, f becomes a function that squares its input (x ** 2).
# Create g by calling ghar(3):

# When ghar(3) is called, it returns a new function actual where num is set to 3.
# So, g becomes a function that cubes its input (x ** 3).
# Call f(3):

# f(3) calculates 3 ** 2, which is 9.
# The output is 9.
# Call g(4):

# g(4) calculates 4 ** 3, which is 64.
# The output is 64.