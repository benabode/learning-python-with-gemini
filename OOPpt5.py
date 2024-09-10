'''
Task 5 - Basic library management system
Goal:
- Create book with attribute: title, author, ISBN and availability 
- The library should be able to: 
    Add books 
    Search for books
        By Title
        By Author
        By ISBN
    Borrow books
    Return books.
'''

class Book:
    def __init__(self, title, author, isbn, is_available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book) #Adds book to empty list.

    def search_Book(self, input):
            match input:
                case "1":
                    print("Searching by Title...")
                case "2":
                    print("Searching by Author...")
                case "3":
                    print("Searching by ISBN...")
                case _:
                    print("Error.")


myLibrary = Library() #Create the empty list for "books" in class "Library"
book1 = Book("The Lord of the Rings", "AuthorName", 12345, True) #Creates new book
myLibrary.add_book(book1) #Method inside library, function that takes value of book1 and puts it in list

userInput = input("Search by 1. Title, 2. Author, 3. ISBN. Enter value: ")
myLibrary.search_Book(userInput)
