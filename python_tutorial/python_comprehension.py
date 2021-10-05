#dictionary comprehension
dict={i:f"item { i }" for i in range ( 1,10001) if i%100 ==0}   # comprehension is the bestb way to code in one line
print(dict)

#list comprehension
lst = [i  for i in range (100) if i%3 ==0]
print(lst)


#set comprehension
dres ={dress for dress in ["dress1","dress2","dress1","dress1"]}
print(dres) #set is nothing it just return only one single element 

#generator comprehension

even = ( i for i in range(100) if i%2==0) #it is called generator 
print(even.__next__()) #by this you can only find single result 
print(even.__next__()) #by this you can only find single result 

for item in (even):   #here you can find directly
    print(item)



