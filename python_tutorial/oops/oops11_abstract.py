from abc import ABC , abstractclassmethod


class shape(ABC):
    @abstractclassmethod
    def printarea(self):
        return 0

class rectangle(shape):
    type = "rectangle"
    sides =4 
    def __init__(self,len,bre):
        self.length = len
        self.breath = bre
    # def printarea(self):
        return self.length*self.breath


rec=rectangle(50,60)
print(rec.printarea())
       
