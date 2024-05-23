str="kya hal chal"
print(str.find("k"))# it will print where the word is located and print its index value

str=str.capitalize() # it will store the capitalized string in the same variables and then can be printed later 
print(str)

print(str.endswith("hal")) # will print true cause its last word is hal

print(str.endswith("ok")) # will print false cause it dont end with ok 

print(str.capitalize()) # will print a new value and then capitalize its a new string 

print(str.replace("a","o")) # every "a" inside the str variable will be now replaced with o 

print(str.replace("hal chal","halli challi")) # hal chal will be replace with halli challi 

print(str.find("k")) # prints -1 cause of the previous codes has changed the code block in certain ways  and its not a valid words as per the code so it prints -1 as an error or something 

print(str.count("a")) # this will print how many times the given value is in the string 