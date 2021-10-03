#here  we have to build a library 
"""
that display book
land aboo
add book
return book
make a attribute 
(lsit of book, library name
and make a dictionary"""


class library:


    def __init__(self,list_of_books,libholder):
        self.list_of_books = list_of_books
        self.librarayholder = libholder
    
    @property
    def display(self):
        print(f"librarian {self.librarayholder}  librarian having books {self.list_of_books}")

    @display.setter
    def display(Self,string):
        return Self.list_of_books + string.split[","]
        



if __name__ =="__main__":

    sandeep = library(["chetan bhagat","harryporter","richdad poordad","time management","attitude"], "sandeep library") 
    sandeep.display = "araybhata,ramajun,elon musk ,the fairy tails"
    print(sandeep.display)
    
    

