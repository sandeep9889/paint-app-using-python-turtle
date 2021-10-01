lst = ["56","54","86"]
for i in range(len(lst)): #har jagah for loop chalana acha nahi h jb apn single line m kre sakte h jaise ki map function
    lst[i] = int(lst[i])
lst[2] = lst[2]+1
print("by loop",lst[2]) 


lst=list(map(int,lst))   #map  m pahela argument jo h vo jo krna chahte ho like if you want to integer it and 2nd jo kis pr krna chahte ho vo h
                        #aur map jo hota h vo ek obj hota h to usko list  m convert krdo
lst[2] = lst[2]+1
print("by map function",lst[2])      



#another other use of map function  with lambda function
num = [2,4,5,6,1,2,3,52]
num = list(map(lambda x:x*x,num))

print(num)


# another use of map function

def sq(a):
    return a*a

def cube(a):
    return a*a*a
func = [sq,cube]
for i in range(5):
    val = list(map(lambda x:x(i),func))
    print(val)
