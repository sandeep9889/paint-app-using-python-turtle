
# Public - like paste papper outside the door of your home
# Protected -  inside your home
# Private - inside your room 

class Employee:
    no_of_leaves = 8
    var = 8 #public variable
    _protec = 9 #protected
    __pr = 98 #private

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

emp = Employee("harry", 343, "Programmer")
print(emp._Employee__pr) #it is printing of protected variable
