with open("/home/dhiren/Documents/Codes/Python/MODULess/sample.txt", "r") as f :
    data = f.read()
    print(data)
    
    num = ""
    for i in range (len(data)):
        if(data[i]==","):
            print(num)
        else:
            num += data[i]
            