#snake water gun game
import random
list = ["S","W","G"]
c  = random.choice(list)
n=1
while(n<10):
    inp= input("slect the operator S :snake W :water, G:gun:")
    def comp(c):
        if(c == "S"):
            if( inp == "S"):
                print("draw the chance")

            elif( inp == "W"):
                print("comp win the chance")   

            elif( inp == "G"):
                print("you win the chance")       
        if(c == "W"):
            if( inp == "S"):
                print("com win the chance")

            elif( inp == "W"):
                print("draw")   

            elif( inp == "G"):
                print("you win the chance")  

        if(c == "G"):
            if( inp == "S"):
                print("com win the chance")

            elif( inp == "W"):
                print("you ein")   

            elif( inp == "G"):
                print("draw the chance")
    n = n+1            


print("welcome to swg game")
print(comp(c))                        
