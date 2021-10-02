class Employ:
    no_of_leaves = 8
    # def __init__(self,asalary,arole) -> None:     #here __init__ is constructor of class 
        # pass

    def printdetails(self):
        return (f"name  {self.name} and  salary is {self.salary} role is {self.role}")        

        

sandeep =Employ()
# sandeep=Employ("sandeep","30k","developer")     #if any attribute written on class like employ so here salaray role  goes to init function and handel it  # attribute in class handel by init function
sandeep.name= "sandeep" 
sandeep.salary = "30k0"
sandeep.role = "developer"


print(sandeep.printdetails())

