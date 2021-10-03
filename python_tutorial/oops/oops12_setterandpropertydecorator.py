
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property  #it is directly set to main attribute 
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter   #here setter can set the name and many m ore
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


hindustani_supporter = Employee("Hindustani", "Supporter") #herer attribute goes to employ class
# nikhil_raj_pandey = Employee("Nikhil", "Raj")

print(hindustani_supporter.email)  #here web can print email from email function  or here can use .email insted of .email()because of property decoder

hindustani_supporter.fname = "US" #here we can change fname

print(hindustani_supporter.email) 
hindustani_supporter.email = "this.that@codewithharry.com"  #herer we have set  email by use of email @setter decoder
print(hindustani_supporter.fname)

del hindustani_supporter.email  # here we have delete by using deleter but in deleter we have put name== none
print(hindustani_supporter.email) #here none is come then it will give warning
hindustani_supporter.email = "Harry.Perry@codewithharry.com" #gherer again set the things
print(hindustani_supporter.email) #herer we have print
 
