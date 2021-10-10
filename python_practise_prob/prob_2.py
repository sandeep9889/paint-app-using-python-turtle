#practise prob2
# divide the apples
n= int(input("enter no of apples:"))
mn = int(input("enter minium no of range"))
mx = int(input("enter maximum no of range"))
for i in range (mn,mx):
    if i%n == 0:
        print(f"{i} is divisible by {n}")

    else:
        print(f"{i} isnot divisible by {n}")
           