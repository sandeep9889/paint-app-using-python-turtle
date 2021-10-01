#enumerate can make life easy
#we can also use this



#it is simple process
l1= ["bhindi", "aloo", "chowmein", "kandaa"]
# i =1
# for item in l1:
#     if i%2 is not 0:
#         print(item)
#     i+=1    

#if you want to simple
for index,item in enumerate(l1): #but here index is starting from 0 
    if index%2==0:
        print(item)

