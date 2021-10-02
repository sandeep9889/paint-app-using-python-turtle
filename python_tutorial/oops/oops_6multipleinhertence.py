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

class player:
    no_of_games = 4
    def __init__(self,aname,asalary,arole,agame):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.game = ["cricket"]
    def printdetails(self):
        print(f"name {self.name} slaary {self.salary} role of {self.role} game {self.game}")


class smart_worker(player,Employ):   #so here is multiple inheritence
    language= "cpp"
    def printlanguage(self):
        print(self.language)





sandeep =Employ("sandeep",255,"developer")
shubham =Employ("shubham", 300, "1st develper")

satish = smart_worker("satish",600,"android",["footbal"])
print(satish.printdetails())


