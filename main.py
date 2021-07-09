class Library:
    def __init__(self, listOfBooks, libraryName) -> None:
        self.books = listOfBooks
        self.name = libraryName

    def displayBook(self):
        for i, book in enumerate(self.books):
            print(f"{i+1} : {book}")

    def addBook(self, newBook):
        return self.books.append(newBook)

    def lendBook(self, personName, nameOfBook):
        if nameOfBook in self.books:
            print(f"{personName} sir, please take your book {nameOfBook}...")
        else:
            print(f"{nameOfBook} this book is not available {personName} sir...")

    def returnBook(self, bookName):
        if bookName in self.books:
            print(f"Thanks for returning {bookName} book sir... Come again....")
        else:
            print(f"sir {bookName} this book is not from our library")


if __name__ == "__main__":
    oxford = Library(["The monk who sold his ferrari","Think and grow rich","Rich dad poor dad","Bhagwad Geeta"], "Oxaford")
    
    # oxford.displayBook()
    # oxford.addBook("Wings of fire")
    # oxford.displayBook()
    # oxford.lendBook("Sanket","Ramayana")
    # oxford.returnBook("Think and grow rich")

    
    print("1. Add Book")
    print("2. Display Books")
    print("3. lend Book")
    print("4. Return Book")

    while(1):
        i = int(input("Enter what do you want : "))
        if(i==1):
            bookName = input("Enter the book name : ")
            oxford.addBook(bookName)
        elif(i==2):
            oxford.displayBook()
        elif(i==3):
            Name = input("Enter the your name : ")
            bookName = input("Enter the book name : ")
            oxford.lendBook(Name,bookName)
        elif(i==4):
            bookName = input("Enter the book name : ")
            oxford.returnBook(bookName)
        else:
            exit()
        

