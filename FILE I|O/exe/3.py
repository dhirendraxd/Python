word ="java" # defining the word that we want to search for 

with open("/home/dhiren/Documents/Codes/Python/MODULess/sample.txt", "r") as f :
    data = f.read()

if(data.find(word) != -1):
    print("found")

else:
    print("not foud")
    
# the above program  search for the words java in that program and if foudn then it will priotn found if not then else 