n=15
i=0
while(i<9):
    print("game by sandeep")
    inp= int(input("enter your number:"))
    if(n>inp):
        print("you are less then actuall")
        continue
    elif(n<inp):
        print("you are more then actual")
        continue
    elif(n == inp):
        print("congo you win the game")
        break
