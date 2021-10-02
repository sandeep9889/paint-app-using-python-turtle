class Employ:
    no_of_leaves= 8
    def __init__(self,aname,asalary,arole):     #here __init__ is constructor of class 
         self.name = aname
         self.salary = asalary
         self.role = arole

    @classmethod  #it can change value of class variable by instance variable
    def change_leaves(cls,newleaves):
        cls.no_of_leaves= newleaves

    @classmethod 
    def dashremover(cls,string):
        return cls(*string.split("-"))


    @staticmethod   #this is static method which doesw not use any clasesmethod and class instance
    def printany(string):
        print("this is very good boy:",string) 
        return   



# sandeep =Employ("sandeep",255,"developer")
# sandeep.change_leaves(25)   #it can be use class varible by instance variable using function @classmethod
# print(sandeep.no_of_leaves)
# sandeep.printany("sanday")

sandeep=Employ.dashremover("sanday-325-student")
print(sandeep)


