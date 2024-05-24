# wap to ask the user to enter names of their fav movies and store them in a list 
facmov = []
facmov.append(input("enter a movei you liked :\n"))
mov1 = input("enter the movie 1 u like")
mov2 = input("enter movie 2 ")
mov3 = input("enter movies 3")

# Append each movie to the list
facmov.append(mov1)
facmov.append(mov2)
facmov.append(mov3)

print(facmov)

# mov = input("enter the movie 1 u like")
# facmov.append(mov) 
 # this can also work appending the movies when they are taken as input  
 
 #wap to checek if a  list containa a palindrom of elements using copy 
 
palin = [1, 3, 4, 5, 4, 3, 1]

copypalin = palin.copy()

palin.reverse()

if copypalin == palin :
    print("palindro")
else :
    print("not palidro")
    
  
  
        #  proper approach without any errors 
          
    # Original list
palin = [1, 3, 4, 5, 4, 3, 1]

# Copy the list
copypalin = palin.copy()

# Reverse the original list
palin.reverse()

# Compare the copied list with the reversed list
if copypalin == palin:
    print("palindro")
else:
    print("not palindro")

#wap to count the num of students with a greae in following tuple 
stud = ["c", "d", "a", "a", "b", "b", "a"]

stud.sort() # easier method
print(stud) # easier approach

result = stud.count("a")
print(result)

sortresul = sorted(stud) #using sorted function and then passing the arguments will store the valeus in the variable
print(sortresul)

sortresul = stud.sort() #this will store the value of none cause the function works like that 
print(sortresul) # this will print none 

std = sorted(stud, reverse=True) # now this will store the descending value reversed instead of none 

print(std)
std = stud.sort(reverse=True)
print(std) # this will also store none 

