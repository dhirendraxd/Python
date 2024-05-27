list = [12, 32, 43, 53, 65, 664, 64]

for numbers in list :
    print(numbers) # this will print all the values inside the list 
    
listt = "dhirendra"
for number in listt :
    print(number)  # this will print all the characteer single word wise 

else : # using else in for loop is completely optional
    print("end ")


num = [12, 32, 42, 42, 42, 52, 532]
x = 43
idx = 0
# for sum in num : # the num in this loop is assigned to each the values of the num and in each iteration its value changes so it can print that  
#     print(sum)
    
for sum in num: 
     if sum == x : 
        print("found ",idx)
        break
    idx +=1
        