print("0enter no 1")

num1= (input())
print("enter no 2")
num2=(input())
try:    #here  try will work on it if is possible then it will run otherwise it will work to another accept it does stop our progrramme
    print("teh sum of number is",int(num1)+int(num2))
except Exception as e: #here if num1=45 and num2=hj then try was not working then try except as e will be on 
    print(e)


print(("this line is very imp"))
