from abc import ABC , abstractclassmethod

#the use of abstract method that in supper class it should be pressureised to child class do any work like an function
class shape(ABC):
    @abstractclassmethod
    def printarea(self):   #here this is forced function in class rectangle
        return 0

class rectangle(shape):
    type = "rectangle"
    sides =4 
    def __init__(self,len,bre):
        self.length = len
        self.breath = bre
    def printarea(self):
        return self.length*self.breath


rec=rectangle(50,60)
print(rec.printarea())
       
