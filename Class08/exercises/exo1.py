# 1. identify visibility intent
class User:
    def __init__(self, username, email, password_hash):
        self.username = username
        self.__email = email
        self.__password_hash = password_hash

# which attributes are public? which are intended for internal use?
# email and pass are for internal use, while username is public.
# 2. redesign the following class to improve encapsulation
class Course:
    def __init__(self, title, seats):
        self.title = title
        self.__seats = seats


# 3. Create StudentAccount class:

# public username
# internal __credits
# methods: add_credits() - use_credits() - show_credits()

class StudentAccount:
    def __init__(self, username, credits):
        self.username = username
        self.__credits = credits

    def add_credits(self, amount):
        self.__credits += amount

    def use_credits(self, amount):
        if self.__credits >= amount:
            self.__credits -= amount
            print(f"{amount} credits used. Remaining credits: {self.__credits}")
        else:
            print("Not enough credits.")

    def show_credits(self):
        print(f"Current credits: {self.__credits}")
student_account = StudentAccount("student1", 100)
student_account.add_credits(50)
student_account.show_credits()
student_account.use_credits(30)
student_account.show_credits()
# 4. Create a MovieTicket class:
# public movie_title
# internal available_seats
# methods: book_seat() - cancel_seat() - show_status()

class MovieTicket:
    def __init__(self, movie_title, available_seats):
        self.movie_title = movie_title
        self.__available_seats = available_seats

    def book_seat(self):
        if self.__available_seats > 0:
            self.__available_seats -= 1
            print(f"Seat booked for '{self.movie_title}'. Remaining seats: {self.__available_seats}")
        else:
            print(f"Sorry, no seats available for '{self.movie_title}'.")

    def cancel_seat(self):
        self.__available_seats += 1
        print(f"Seat cancelled for '{self.movie_title}'. Available seats: {self.__available_seats}")

    def show_status(self):
        print(f"Movie: {self.movie_title}, Available Seats: {self.__available_seats}")

movie = MovieTicket("Inception", 5)
movie.show_status()
movie.book_seat()
movie.show_status()
movie.cancel_seat()
movie.show_status()