#this is our first oops programming code 
class student:       #here  we initialize a class
    pass                     #pass means noting to do


sandeep = student()  #this is an object
kumar  =student()
sandeep.name = "sandy"   #this is instance variable that has to build in classs
sandeep.clg = "sati"
sandeep.branch = "aiads"
kumar.name = "shiv"
kumar.clg  = "baktara sarkari"
kumar.branch = "cse"
kumar.subject = ["coa","dsa"]

print(sandeep.name,sandeep.clg,kumar.clg,kumar.subject)
