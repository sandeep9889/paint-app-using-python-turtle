a = input("what is your name")
b = int(input("how much you earn"))
key = [1,2,3]
c = int(input(f"enter key from {key}"))
if c != 1 and c!=2 and c!=3:
    raise KeyError("you wrong input")
if b ==0:
    raise ZeroDivisionError("B is 0 stopping the programme")
if a.isnumeric():
    raise Exception("numbers are not allowed")

print(f"hello {a}")