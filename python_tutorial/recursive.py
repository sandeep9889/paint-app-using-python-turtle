#here  we have to build recursive funvction
#n*(n-1)!
# def recursive():
#     if num==1:
#         return 1
#     else:
#         return num * recursive(num-1)
        

# num = int(input("enter a number :"))
# print("by recursion",recursive(num))



#for febonacci series
# 0 1 1 2 3 
def fibonacci(n):
    if n==0:
        return 0 

    elif n==1:
        return 1

    else:
        return fibonacci(n-1) + fibonacci(n-2)       
num = int(input("enter no of fibonacci series:"))
print(fibonacci(num))
    