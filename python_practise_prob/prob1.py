#practce problem 1
# age proble



age = int(input("enter your age or birthdate:"))
present_date = 2021
if len(str(age))>3: #it mena he put birthdate
    #present age - real age
    h=  present_date - age 
    
    if age>2021:
        print("sorry you are not born entr correct input ")

    elif int(h)<100:
        print("you are less then 100year")
        remain = 100-h
        print(f"{remain} years remain")
        print( present_date + remain ,"inyear you will become 100year old")

elif len(str(age))<3 and len(str(age))>0: 
    h1=100-age
    print("remianig age to become 100:",h1)
    h3 = present_date + h1 
    print(f"in year {h3} you become 100" )







