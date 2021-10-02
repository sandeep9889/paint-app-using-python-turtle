class Employ:
    no_of_leaves = 8
    def __init__(self,aname,asalary,arole):     #here __init__ is constructor of class 
         self.name = aname
         self.salary = asalary
         self.role = arole

    def printdetails(self):
        return (f"name  {self.name} and  salary is {self.salary} role is {self.role}")        

        

sandeep =Employ("sandeep",255,"developer")#if any attribute written on class like employ so here salaray role  goes to init function and 

# sandeep=Employ("sandeep","30k","developer")     handel it  # attribute in class handel by init function
# sandeep.name= "sandeep" 
# sandeep.salary = "30k"
# sandeep.role = "developer"
print(sandeep.printdetails())


print(sandeep.role)

