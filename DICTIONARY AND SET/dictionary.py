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

# null dictionary 
nulldict = {
    # codes 
}

# printing the data inside dictionary 
print(type(infor))
print(infor["name"])
print(infor["is_adult"])
print(infor["topics"])
infor["topics"] = "joe"
print(infor["topics"])