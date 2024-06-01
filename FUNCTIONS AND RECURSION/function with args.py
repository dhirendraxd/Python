def sumall(*args): # this indicates that there are multiple values comming in this function so it is used as an preinformant in function 
    
    # if we dont use *args and only use args then it will only take an single value and then show erros cause of the user entering multiple vlaues in it
     print(*args)
     
    #  for i in args:
    #      print(i * 2)
         
     return sum(args)

print(sumall(1, 3, 4))
print(sumall(43,43)) 
print(sumall(43, 43, 53, 523, 52, 12, 43, 5)) # we can also add this using an sigle funciotn 

#output by : print(*args) :

1 3 4 :
8
43 43 :
86
43 43 53 523 52 12 43 5 :
774
          