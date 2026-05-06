class Book:
    title = "Unknown Title"
    author = "Unknown Author"
    available = True
    library_name = "Central Library"
    def __init__(self, title, author,available):
        self.title = title
        self.author = author
        self.available = available
    
    @classmethod
    def change_library_name(cls, new_name):
        cls.library_name = new_name
    
    @staticmethod
    def is_valid_title(title):
       if(len(title) > 0):
           return print("Valid title")
       else:
           return print("Invalid title")
    
    
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
        print(f"The Title of the book is :  {self.title} for the author: {self.author}, and it's availability is : {self.available}")