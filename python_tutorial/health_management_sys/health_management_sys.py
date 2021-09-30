#health management system exercise 5 
#here webhave 3 person sandeep  hemant and rahul
import datetime
def getdate():
    return datetime.datetime.now()

def take(k):
    if k ==1:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c ==1):
            value=input("type here/n")
            with open ("sandeep_ex.txt","a",)as op:
                op.write(str([str(getdate())])+":"+value+"/n")

            print("succesfully  written")

        elif(c ==2):
            value1 = input("type here/n")
            with open("sandeep_fd.txt","a") as op:
                op.write(str([str(getdate())])+":"+value1)

            print("succesfully writen")


    if k ==2:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c ==1):
            value=input("type here/n")
            with open ("hemant_ex.txt","a",)as op:
                op.write(str([str(getdate())])+":"+value+"/n")

            print("succesfully  written")

        elif(c ==2):
            value1 = input("type here/n")
            with open("hemant_fd.txt","a") as op:
                op.write(str([str(getdate())])+":"+value1)

            print("succesfully writen")            



    if k ==3:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c ==1):
            value=input("type here/n")
            with open ("rahul_ex.txt","a",)as op:
                op.write(str([str(getdate())])+":"+value+"/n")

            print("succesfully  written")

        elif(c ==2):
            value1 = input("type here/n")
            with open("rahul_fd.txt","a") as op:
                op.write(str([str(getdate())])+":"+value1)

            print("succesfully writen")            






def retrive(k):
    if k ==1:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c ==1):
            value=input("type here/n")
            with open ("sandeep_ex.txt")as op:
                for i in op:
                    print(i, end="")

            

        elif(c ==2):
            value1 = input("type here/n")
            with open ("sandeep_ex.txt")as op:
                for i in op:
                    print(i, end="")


    if k ==2:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c ==1):
            value=input("type here/n")
            with open ("hemant_ex.txt")as op:
                for i in op:
                    print(i, end="")

            print("succesfully  written")

        elif(c ==2):
            value1 = input("type here/n")
            with open ("hemant_ex.txt")as op:
                for i in op:
                    print(i, end="")

            print("succesfully writen")            



    if k ==3:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c ==1):
            value=input("type here/n")
            with open ("rahul_ex.txt")as op:
                for i in op:
                    print(i, end="")

            print("succesfully  written")

        elif(c ==2):
            value1 = input("type here/n")
            with open("rahul_fd.txt","a") as op:
                op.write(str[str(getdate())]+":"+value1)

            print("succesfully writen")   



print("Welcome to health management system")
inp = int(input("if you want to take press 1 else want to retrive press 0:"))
if(inp == 1):
    people = int(input("for sandeep:1 for hemant 2 for rahuk :3"))
    take(people)
elif(inp == 0):
    people_retrive = int(input("for sandeep:1 for hemant 2 for rahuk :3"))
    take(people_retrive)

else:
    print("give proper input")    
        

