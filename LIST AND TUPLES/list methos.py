listt = [3, 4, 6, 4]
listt.append(4)
print(listt) # added 4 in the list array and the ouput will print along with 4 inside it 

               # sorting

sor = [1, 5, 3, 4, 2]
sor.sort()
print(sor.sort()) #this wont return any values it will only make changes to the exisitin array and then we have to print it seperately
print(sor)

# reverse sorting will return sorted values from backwards 
revs = [ 3, 4, 5, 6, 1, 2]
revs.sort(reverse=True)
print(revs)

 #rev sorting for characters
rech = ['a', 'b', 'f']
rech.sort(reverse=True)
print(rech) #prints f b a 
rech.sort() # sorting them ascending  way
print(rech) # printing the ascending  order 

                # reverse  
revli = ['a', 'v', 'b']
revli.reverse()
print(revli)  # output  b v a 


                     #insert
lisinsert = [2, 3, 5, 6,  66]
lisinsert.insert(2, 'else') # adds else in the 3rd position of the array 
print(lisinsert) # ouput : [2, 3, 'else', 5, 6, 66]


                         #remove
lesre = [3, 5, 55, 23]
lesre.remove(5) # will remove the 5 form the array but only the first occurance not more then one 
lesre.pop(2) #remove the 3rd values inside the array 
print(lesre)
