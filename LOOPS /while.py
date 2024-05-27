count = 1
while count <= 1 :
    print("hello")
    count += 1 
    
i = 1
while i<=5 :
    print("hey")
    i+=1 # we use this operator to increase the value of that variables to increase iteration 
i2 = 5
while i2 >= 1 :
    print("loop ended")
    if i2== 3 :
        print("ended at 3 ") 
        break # the program will stop at 3 when it hits 3
    i2 -= 1
    
    i2 = 5
while i2 >= 1 :
    print("loop ended")
    if i2== 3 :
        print("escaped at 3 ") 
        continue #  the 3rd will skip and next will print but not 3 will print 
    i2 -= 1
    