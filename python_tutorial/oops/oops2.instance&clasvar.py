#here we can diffrentiaite classes and instance variable

class Employ:
    no_of_leaves = 8  #his is class var
sandeep = Employ()
jatin = Employ()


#these are instance variable
sandeep.name = "sandeep"    
sandeep.salary = "30k"
sandeep.role  = "associate"


jatin.name = "jatin"
jatin.salary = "40k"
jatin.role = "developer"




print(sandeep.no_of_leaves)  #we can open class vsariable by object also

Employ.no_of_leaves = 10
print(Employ.no_of_leaves) #it can posssible
  
sandeep.no_of_leaves = 12 #it can not posiible because we have change class variable it is not possible by object
# but can create its own object variable

print(Employ.no_of_leaves)

print(sandeep.__dict__)  #herer dicrt func tion use to find no of vartible define


