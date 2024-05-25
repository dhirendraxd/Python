infor = {
    # adding list and tuples
    "subjects" : ["python", "java" ],
    "topics" : ("dict", "set"),
    "key" : "value",
    "name" : "dhirendra",
    "age" : 23,
    "is_adult" : True,
    "marks" : 5.6,
    
}
print(infor.keys())  # this will print the keys inside the dictionary but wont print the nested ones >

print(list(infor.keys())) # typecasting these into list using  list will print them in a list 

print(len(infor.keys())) # this will print the length of the dictionary :7

print(infor.values()) # this will print the values inside the keys given in dictionary 

print(list(infor.values())) # this will put the values in a listed way while printing 

prinst = (list(infor.items()))  # this will retunr the pair of key and values inside a bracket 
    #  output: dhirendra'), ('age', 23), ('is_adult', True), ('marks', 5.6)])
    
print(prinst[0])

print(infor.get("name"))#incase there is no any key named name it willl return NONE as an ouput 

print(infor.update({"city" : "delhi"})) # we can also add new key and values using .update

nedict = {
    "dhiren" : "code",
    "key" : 2332, # the key value already exist so it will replace with newone
}
infor.update(nedict) # we can  update the existing dict with a new dict and indicidual value
print(infor)