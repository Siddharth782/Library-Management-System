#Declaring Library class and it's attributes
class Library:
    
    def __init__(self, list):
        self.listofBooks = list

    def availableBooks(self):
        print("The books available in the library are: ")
        for books in self.listofBooks:
            print(f"* {books}")
        print("\n")

    def borrowBook(self, bookName):
        if bookName in self.listofBooks:
            print(f"You have borrowed book {bookName}. Please return it in 30 days.")
            self.listofBooks.remove(bookName)
        else:
            print(f"{bookName} is presently not available in the library. Please wait till it's returned to library.")
        print("\n")

    def returnBook(self, bookName):
        self.listofBooks.append(bookName)
        print("Your book has been returned. Thanks for using Central Library.")
        print("\n")

    def donateBook(self,bookName):
        if bookName in self.libraryCollection:
            print("This book is already present in Central Library.")
        else:
            self.libraryCollection.append(bookName)
            # self.listofBooks.append(bookName)
            print("Thanks for donating the book to Central library.")        
        print("\n")

    def AllBooks(self):
        print("The books available in the library are: ")
        for books in self.libraryCollection:
            print(f"* {books}")
        print("\n")

#Declaring Student class and it's attributes
class Student:

    issues = {}

    def __init__(self, id):
        if id in self.issues.keys():
           print("Select a different id") 
        else:
           print("Central Library welcomes the new member")
           updateIssues = {
            id: []
           }
        self.issues.update(updateIssues)

    def borrowBook(self):
        self.book = input("Enter the book you wanna borrow from library: ")
        updateIssues = {
            id: [{self.book}]
           }
        self.issues.update(updateIssues)
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
    s = Student(34)
    
    wlcmMsg = '''   Welcome to Central Library    \n'''
    print(wlcmMsg)
    print("Are you a New Member(n) or Existing Member(e)? ")
    member = input()
    if member == "e":
        id = int(input("Enter your id: "))
        if id in Student.issues.keys():
            choices = '''1. Display all the books available in library.
2. Borrow a book
3. Return a book
4. Donate a book
5. Display your borrowed books
6. Exit from Library
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
                elif a == 5 :
                    Student.issues.get(id)
                elif a==6:
                    print("Thanks for visiting here!!")
                    exit()
                else:
                    print("invalid Choice")
        else:
            print("This member doesn't exist. Do you want to get membership?")

    elif member == "n":
        x = int(input("Enter a unique id code: "))
        z = Student(x)
        choices = '''1. Display all the books available in library.
2. Borrow a book
3. Return a book
4. Donate a book
5. Display your borrowed books
6. Exit from Library
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
            elif a == 5 :
                Student.issues.get(id)
            elif a==6:
                print("Thanks for visiting here!!")
                exit()
            else:
                print("invalid Choice")