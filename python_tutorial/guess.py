n=15
i=0
while(i<9):
    inp = int(input("enter a no"))
    if n > inp:
        print("you are less then actual ")
        i=i+1
        continue
    elif n < inp:
        print("you are greater then actual")
        i = i + 1
        continue
    elif n == inp:
        print("****congo you win a game and your guess match","\nin given interval ",i)
        i=i+1
        break


