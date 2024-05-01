# Task 1: Library System Enhancement

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def addBook(name, author): # Function to add a new book to library
    new_book = (name, author)
    if new_book in library:
        print("This book is already in the library") # Notify user if book already exists in library
    else:
        library.append(new_book) # Add book to end of library

addBook("Green Eggs on Ham", "Dr. Suess") # Add a new book
print(library) # Print out new library
addBook("1984", "George Orwell") # This won't add a book, since the book already exists in library