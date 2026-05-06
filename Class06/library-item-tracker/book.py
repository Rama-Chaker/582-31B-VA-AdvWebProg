class Book:
    title = "Unknown Title"
    author = "Unknown Author"
    available = True
    def __init__(self, title, author,available):
        self.title = title
        self.author = author
        self.available = available
    
    def borrow(self):
        if self.available:
            self.available = False
            print(f"You have borrowed '{self.title}' by {self.author}.")
        else:
            print(f"Sorry, '{self.title}' is currently not available.")
     
    def return_book(self):
        if self.available == False:
            self.available = True
            print(f"You have returned '{self.title}' by {self.author}.")
        else:
            print(f"'{self.title}' was not borrowed.")

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Available: {self.available}")