# always remember  count starts form 0 in programming 

strname= "dhirendra"
str=strname[0]
print(str)
print(strname[3]) # WE CANT MANIPULATE THE VALUES IN IT LIKE THIS ONLY DISPLAYING IS POSSIBLE 

# SLICING
# STR[startingindex: endingindex]  ending index ins not included 
name="mondler" # the in between values  will print 
print(name[1:4]) # first index wont print but the last index always prints 

print(name[1:len(name)]) # len(name) will print till the last character of the string form 1:end 

print(name[1:]) # we can also write 1: only it will print till the last on it own 

print(name[:7])  # it will now print values form 0 to the given number 7  by itself\
    