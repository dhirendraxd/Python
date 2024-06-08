fil = open("clasher.js", "r+")

fil.write("(this file was created )") # this will now overwrite the file from the very first line 

print(fil.read()) # (this file was created )  : this wont print cause  we have  overwrite (this file was created )  previously while (this file was created ) ...so it wont count that it will count the unchanged things while printing 

fil.close


