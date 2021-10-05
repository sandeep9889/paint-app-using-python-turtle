#dictionary comprehension
dict={i:f"item { i }" for i in range ( 1,10001) if i%100 ==0}   # comprehension is the bestb way to code in one line
print(dict)

#list comprehension
lst = [i  for i in range (100) if i%3 ==0]
print(lst)


#set comprehension
dres ={dress for dress in ["dress1","dress2","dress1","dress1"]}
print(dres)