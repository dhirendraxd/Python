tc = {
    "table" : ["a piece of furniture","list of facts and figures"],
    "cat" : "small animal"
}
print(tc)

classset = {
    "java" ,"java", "python", "c++", "java", "python", "c", "c","javascript","js"}
print(len(classset))


subjec = {}
x = int(input("enter marks 1"))
subjec.update({"math":x})

z = int(input("enter marks 2"))
subjec.update({"chem":z})

y = int(input("enter marks 3"))
subjec.update({"phy":y})

print(subjec)

value = {
    9, 9.0
}
print(value) #output 9 cause 9 and 9.0 are same  but if we use 9.4 then it will pritn both cause nearest value of 9 is 9.0 so


valuee = {
 (  "float", 9.0)
 , ("int", 9)
}
print(valuee)