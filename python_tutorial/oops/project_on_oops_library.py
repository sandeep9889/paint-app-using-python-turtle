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


sandeep = library(["chetan bhagat","harryporter","richdad poordad","time management","attitude"], "sandeeplibrary")   
print(sandeep.list_of_books) 