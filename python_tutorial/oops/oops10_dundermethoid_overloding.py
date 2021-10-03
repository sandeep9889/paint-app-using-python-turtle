#here we use dunder  ,method   dunder method is that is use to be get attribute 
#every dunder method start from __     __ like this 
"""
many dunder methood as follows

# print our string object
    def __repr__(self):

def __add__(self, other):
        return self.string + other
        and many more

Addition

a + b

add(a, b)

Concatenation

seq1 + seq2

concat(seq1, seq2)

Containment Test

obj in seq

contains(seq, obj)

Division

a / b

truediv(a, b)

Division

a // b

floordiv(a, b)
        
"""




class Employee:
    no_of_leaves = 8
    

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)
        
    def __add__(self,other):    #it is a dunder method
        return self.salary+other.salary

    def __truediv__(self,other):
        return self.salary / other.salary   

    def __repr__(self):   #it will be use in return emp whn you print(emp)
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
      
emp = Employee("harry", 343, "Programmer")
emp1 = Employee("rohan", 34, "swipper")

print(emp+emp1)
print(emp/emp1)
print(emp) #it should furthur return object bbut now it should return from repr dunder method 