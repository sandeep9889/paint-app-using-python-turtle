#here  we have to build a library 
"""
that display book
land aboo
add book
return book
make a attribute 
(lsit of book, library name
and make a dictionary"""


from _typeshed import Self


class library:


    def __init__(self,list_of_books,libholder):
        self.list_of_books = list_of_books
        self.librarayholder = libholder
        self.lendict = []

        
    def lendin(self,user,book):
        if book not in self.lendict.key:
            self.lendict.update({book:user})
            print("lender book data base has been updated . you can take the book now")
        else:
            print(f"the book has beeen issued by {self.lendict[book]}")    
        

    def returnbook(self,user,book):
        self.list_of_books.remove(book)
        print(f"book {book} has been return by {user}")

    def addbook(self,book):
        Self.list_of_book.append(book)
        print(f"book has been added to book_list")

    @property
    def display(self):
        print(f"we have library {self.librarayholder} ")
        for book in self.list_of_books:
            print(book)

    @display.setter
    def display(Self,string):
        # return Self.list_of_books + string.split[","]
        pass
        



if __name__ =="__main__":

    sandeep = library(["chetan bhagat","harryporter","richdad poordad","time management","attitude"], "sandeep library") 
    sandeep.display = "araybhata,ramajun,elon musk ,the fairy tails"
    print(sandeep.display)
    
    

