count = 0
with open("/home/dhiren/Documents/Codes/Python/MODULess/sample.txt", "r") as f:
    data = f.read()
    print(data)
   
    nums = data.split(",")
    for val in nums:
        try:
            if int(val) % 2 == 0:
                count += 1
        except ValueError: # not necessaraly to use but useful when error handling 
            pass

print(count)

   #sctrach logic 
    # num = ""
    # for i in range (len(data)):
    #     if(data[i]==","):
    #         print(num)
    #     else:
    #         num += data[i]
    #         print("ya kya ha bc ")