def evengen(limit):
    # li = []
     for i in range(2, limit + 1, 2):
        #  li.append(i)
        yield i
#yeild is used to retunr value  and it store value in memory and generate prodcues values on demand efficiently without storing all values in memory at once 

# x =print( evengen(34))
for num in  evengen(10):
    print(num)