from typing import BinaryIO


inp = int(input("enter how many rows starL:" ))
inp1 = bool(int(input("which start pattern you want if upward press any except 0 and for downward press 0:")))
i=1
j=1
if(inp1 == True):
    while(i<inp):
        for j in i:
            print("*")
            i= i+1

elif(inp1 == False):
    for i in inp:
        for inp  in 0 :
            print("*")
            i= i+1