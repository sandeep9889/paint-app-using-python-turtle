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
        self.lendict={}

        
    def lendin(self,user,book):
        if book not in self.lendict.key():
            self.lendict.update({book:user})
            print("lender book data base has been updated . you can take the book now")
        else:
            print(f"the book has beeen issued by {self.lendict[book]}")    
        

    def returnbook(self,user,book):
        self.lendict.pop(book)
        print(f"book {book} has been return by {user}")

    def addbook(self,book):
        self.list_of_books.append(book)
        print(f"book has been added to book_list")

    @property
    def display(self):
        print(f"we have library {self.librarayholder} ")
        for book in self.list_of_books:
            print(book)

    
        



if __name__ =="__main__":

    sandeep = library(["chetan bhagat","harryporter","richdad poordad","time management","attitude"], "sandeep library") 
    

    while(True):
        print(f"welcome to the {sandeep.librarayholder} libraray.enter your choice to continew")
        print("1 . display books")
        print("2 . lend books")
        print("3 . add a book")
        print("4 . return a books")
        user_choice = int(input())
        if user_choice not in [1,2,3,4]:
            continue
        else:
            user_choice = int(input())

        if user_choice ==1:
            sandeep.display
        elif user_choice ==2:
            book = input(f"enter the name of the book from given books {sandeep.list_of_books}")
            user =input("enter your name")
            sandeep.lendin(user,book)

        elif user_choice ==3:
            book = input("enter the name of the book you wwant to add")

            sandeep.addbook(book)

        elif user_choice ==4:
            book = input("enter the name of the book you wwant to return")
            sandeep.returnbook(book) 

        else:
            print("not a valid option")

        print("press q for quit and c for continew")
        user_choice2=""
        while(user_choice2!="c" and user_choice2 !="q"):
            user_choice2 = input()
            if user_choice2=="q":
                exit()
            elif user_choice2 == "c":
                continue  


        


