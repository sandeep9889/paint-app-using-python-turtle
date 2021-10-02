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

#inheritence meaning like have same look like in parents 
"""
so in python inheritence it is  a concept in python that having previous class to new classes """




class programmer(Employ):  #here we have initilize single ingheritence

    def __init__(self, aname, asalary, arole, alanguages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages= alanguages

        
    def printdetails(self):
        return (f"programmer name is {self.name} and  salary is {self.salary} role is {self.role} and languages are {self.languages}")

sandeep =Employ("sandeep",255,"developer")
harry = Employ("harray",300,"associate")

shubham = programmer("shubham",500,"programmer",["python"])
karan = programmer("karam",600," 1st programmer",["python","cpp"])
print(karan.printdetails())
