# Library Managment 
class Library:
  def __init__(self):
    self.noBooks = 0
    self.books = []
  def addBooks(self,book):
    self.books.append(book)
    self.noBooks = len(self.books)
  def showInfo(self):
    print(f"The library has {self.noBooks} books. The books are")
    for book in self.books:
      print(book)

 # Creating an instance of Library     
L1 = Library()
# Allowing the user to add books until they type 'exit'
while True:
    book_name = input("Enter the book name to add (or type 'exit' to stop): ").strip()
    if book_name.lower() == "exit":  
        break  # Stop adding books if the user types 'exit'
    L1.addBooks(book_name)
    print(f"'{book_name}' has been added to the library.\n")
L1.showInfo()

    
