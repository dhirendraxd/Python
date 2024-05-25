sett = {34, 53, 52, "hey", "hello"}

sett.add(23) # this is how we can add any number and strings inside set and  it will onits own find place to place them 

sett.add(23) # this value wont print cause its an duplicate value and will count as the same value entered twice 

print(sett) #output :{'hey', 34, 52, 53, 23, 'hello'}

sett.remove(34)  # 34 will be removed from the set and will print without it 

# sett.remove(99) # this will show the key error of 99 cause the value isnt inside this 
print(sett)

print(sett.clear()) # this will empty the whole set and if we print then its length will be 0 

print(sett.pop) # it will randomly pop  any values from the set 
    # in practical senario when we neeed an random value from a set 
seet = {1, 3, 4, 5, 6}  
seet2 = { 1, 3, 4, 5, 7, 8, 9}
seet.union(seet2)  # we can combine or union two sets using .union and it will print a new set using boht the sets 

# it dont make any changes to old sets it only occurs to the new one made older will still have the same values 

print(seet) # output : {1, 3, 4, 5, 6}
                
