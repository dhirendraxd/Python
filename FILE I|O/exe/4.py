def check():
    word = "python"
    data = True
    lineno = 1
    with open("/home/dhiren/Documents/Codes/Python/MODULess/sample.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(lineno)
                lineno += 1

    return -1
check()

#Output : 1 
 # cause we have python multiple python but its only one entity 