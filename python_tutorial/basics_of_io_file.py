# file to basics
"""
"r"= for read mode -default
"w"= write mode
"+" =for read and write mode
"x"= if file was not present then it will build a file
"a"= for appending a file
"""

# f =open("sandeep.txt", "r")
# print(f.readline()) #readline function used to read individual line /
# print(f.readlines())#it can all lines in list and from above read line we have only remaining two line
# content=f.read() # read to read datav
# print(content)
# f.close()


# for write
# f = open("sandeep.txt1","w") #here is no sandeep1.txt file but it will build it self
# f.write("hello sandeep kaise ho")



#for read and write
# f = open("sandeep.txt1","r+")
# san=f.read() #for read
# print(san) 
# f.write("college konsa h aapka aur dewas m kha rahete ho") #it can be write in the sandeep.txt1 file


#to know and reset about where is file pointer location
f = open("sandeep.txt1", "r")
f.readline()
tld=f.tell() #it will give the information wherer is file pointer lie 
reset =  f.seek() #it will reset file pointer like  f.seek(10) so here it will start from 10 index

f.read()

f.close()


