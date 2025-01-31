# Library_Managment
Library Management System

# Overview

This is a simple Library Management System implemented in Python. The program allows users to add books to a library dynamically until they choose to stop. It also displays the total number of books in the library along with their titles.

# Features

Add books to the library dynamically.

User can enter multiple books until they type 'exit'.

Display all books stored in the library.

# How It Works

The program initializes an empty library.

It continuously prompts the user to enter a book name.

The user can add books until they type 'exit'.

Once they exit, the program displays all books stored in the library.

# Usage

Run the Program

To run the program, execute the following Python script:

class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def showInfo(self):
        print(f"\nThe library has {self.noBooks} books. The books are:")
        for book in self.books:
            print(book)

# Creating an instance of Library
L1 = Library()

# Allowing the user to add books until they type 'exit'
while True:
    book_name = input("Enter the book name to add (or type 'exit' to stop): ").strip()
    if book_name.lower() == "exit":  
        break  # Stop adding books if the user types 'exit'
    L1.addBook(book_name)
    print(f"'{book_name}' has been added to the library.\n")

# Display all books added
L1.showInfo()

Example Output

Enter the book name to add (or type 'exit' to stop): Harry Potter
'Harry Potter' has been added to the library.

Enter the book name to add (or type 'exit' to stop): The Alchemist
'The Alchemist' has been added to the library.

Enter the book name to add (or type 'exit' to stop): exit

The library has 2 books. The books are:
Harry Potter
The Alchemist

# Requirements

Python 3.x

# Contributing

Feel free to contribute by improving the functionality, adding features, or optimizing the code!

# License

This project is licensed under the MIT License.
