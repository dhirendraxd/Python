
fil = open("dhiren.c", "r+") # this will write data init but wont let pritn the result 

fil.write("(this file was created for c and this wont display its content while printing its data cause we have used r+ )") 

print(fil.read())  #wont print data casue we used r+

fil.close