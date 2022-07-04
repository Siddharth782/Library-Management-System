#Declaring Library class and it's attributes
class Library:
    
    def __init__(self, list):
        self.listofBooks = list

    # displaying all the books available in library
    def availableBooks(self):
        print("The books available in the library are: ")
        for books in self.listofBooks:
            print(f"* {books}")
        print("\n")
    
    #borrowing book
    def borrowBook(self, bookName):
        if bookName in self.listofBooks:
            print(f"You have borrowed book {bookName}. Please return it in 30 days.")
            self.listofBooks.remove(bookName)
        else:
            print(f"{bookName} is presently not available in the library. Please wait till it's returned to library.")
        print("\n")

     # returning book
    def returnBook(self, bookName):
        self.listofBooks.append(bookName)
        print("Your book has been returned. Thanks for using Central Library.")
        print("\n")

     # donating book to library
    def donateBook(self,bookName):
        if bookName in self.libraryCollection:
            print("This book is already present in Central Library.")
        else:
            self.libraryCollection.append(bookName)
            print("Thanks for donating the book to Central library.")        
        print("\n")


#Declaring Student class and it's attributes
class Student:

    def borrowBook(self):
        self.book = input("Enter the book you wanna borrow from library: ")
        return self.book
        print("\n")

    def returnBook(self):
        self.book = input("Enter the book you wanna return from library: ")
        return self.book
        print("\n")

    def donateBook(self):
        self.book = input("Enter the book you wanna donate to library: ")
        return self.book
        print("\n")



if __name__ == "__main__":
    centralLibrary = Library(["Algorithms", "Data Structures", "Django", "BootStrap", "Machine Learning", "Deep Learning"])
    s = Student()
    
    wlcmMsg = '''   Welcome to Central Library    \n'''
    print(wlcmMsg)
    
    choices = '''1. Display all the books available in library.
2. Borrow a book
3. Return a book
4. Donate a book
5. Exit from Library
'''
            while True: 
                print("Please select from the given choices\n")
                print(choices)
                a = int(input("Enter your choice: "))
                print("\n")
                if a == 1 :
                    centralLibrary.availableBooks()
                elif a==2:
                    centralLibrary.borrowBook(s.borrowBook())
                elif a==3:
                    centralLibrary.returnBook(s.returnBook())
                elif a==4:
                    centralLibrary.donateBook(s.donateBook())
                elif a==5:
                    print("Thanks for visiting here!!")
                    exit()
                else:
                    print("invalid Choice")
 
