# file to basics
"""
"r"= for read mode -default
"w"= write mode
"+" =for read and write mode
"x"= if file was not present then it will build a file
"a"= for appending a file
"""

f =open("sandeep.txt", "rt")
print(f.readline()) #readline function used to read individual line 
print(f.readlines())#it can all lines in list and from above read line we have only remaining two line





# content=f.read() # read to read datav
# print(content)
