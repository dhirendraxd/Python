n = 5 
sum = 0
i =1
# using while  sum of n numbers 
while i < n :
    sum += i 
    i += 1 
    # using for 
for i in range(1, n+1) :
    sum += i
    print(sum)
    

#factorial of first n numbers 
n = 5
fact = 1
i = 1
while i<=n :
    fact*= i 
    i += 1 
    print(fact)
    
# using for 
n=5 
fact = 1

for i in range(1, n+1) :
    fact *= i 
    print(fact)