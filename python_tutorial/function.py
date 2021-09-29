a = 9
b = 41
c = sum((a,b))
# print("your sum is :",c) #build in function function that is to build in  computer


#for initialising for our function we have to use def




def func1(a,b):
    """This function used for taking average""" #it is docstring that should give information about function
    average =(a+b)/2
    return average   #here  return average returns a average that has to be defined in above line 
    
print(func1(5,8))
print(func1.__doc__)  #it can print docstring