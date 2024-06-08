fil = open("clasher.js", "a+")

fil.write("( this is an appending text)") # this will now add this line () after the contents of clasher.js

print(fil.read())  #prints nothign cause we are using a  or its type a+ so but it will add that we can look in the file 
fil.close


#data in clasher.js:
  
  (this file was created ) using code inside io(creating file).py( this is an appending text)