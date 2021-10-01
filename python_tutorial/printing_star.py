from typing import BinaryIO


inp = int(input("enter how many rows starL:" ))
inp1 = bool(int(input("which start pattern you want if upward press any except 0 and for downward press 0:")))
i=1
j=1
if(inp1 == True):
    for i in range(1,inp+1):
        for j in range(i):
            print("*",end ="")
            
        print()    

elif(inp1 == False):
    for i in range(inp,0,-1):
        for j in range(i,0,-1) :
            print("*",end = "")
            
        print()