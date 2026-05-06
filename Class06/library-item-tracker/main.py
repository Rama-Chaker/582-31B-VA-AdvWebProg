from book import Book
book1 = Book("1984", "George Orwell", True)
book2 = Book("To Kill a Mockingbird", "Harper Lee", False)
print(f"Title: {book1.title}, Author: {book1.author}, Available: {book1.available}")
print(f"Title: {book2.title}, Author: {book2.author}, Available: {book2.available}")