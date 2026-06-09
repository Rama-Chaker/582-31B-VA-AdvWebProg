from show_status import ShowStatus
from user import Customer
from show_status import MAX_TICKETS_PER_BOOKING
class MovieShow:
    def __init__(self, title, capacity, booked_seats, status):
        if(title == "" or capacity <= 0 or booked_seats < 0 or booked_seats > capacity):
            raise ValueError("Invalid input for MovieShow")
        if not isinstance(status, ShowStatus):
            raise InvalidStatusError("status must be a ShowStatus value")
        self.__title = title
        self.__capacity = capacity
        self.__booked_seats = booked_seats
        self.__status = status
    @property
    def remaining_seats(self):
        return self.__capacity - self.__booked_seats
    @property
    def capacity(self):
        return self.__capacity
    @capacity.setter
    def capacity(self, new_capacity):
        if new_capacity <= 0:
         raise ValueError("Capacity must be greater than 0")

        if new_capacity < self.__booked_seats:
         raise ValueError("New capacity cannot be less than booked seats.")

        self.__capacity = new_capacity
      
    @property
    def booked_seats(self):
        return self.__booked_seats
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, new_status):
        if not isinstance(new_status, ShowStatus):
            raise InvalidStatusError("status must be a ShowStatus value")
        self.__status = new_status
    def book_tickets(self, customer, quantity):
        if quantity <= 0 or quantity > MAX_TICKETS_PER_BOOKING:
            raise InvalidBookingError(f"Invalid quantity. You can book between 1 and {MAX_TICKETS_PER_BOOKING} tickets.")
        elif ShowStatus.CANCELLED == self.__status:
            raise ShowCancelledError("Cannot book tickets. The show is cancelled.")
        elif ShowStatus.SOLD_OUT == self.__status:
            raise ShowSoldOutError("Cannot book tickets. The show is sold out.")
        elif self.__booked_seats + quantity > self.__capacity:
            raise InvalidBookingError("Not enough seats available.")
        else:
            self.__booked_seats += quantity
            if self.__booked_seats >= self.__capacity:
                self.status = ShowStatus.SOLD_OUT
            return f"{quantity} tickets successfully booked for {customer.name}."
    def cancel_show(self):
        self.status = ShowStatus.CANCELLED
    def display_info(self):
        print(f"Title: {self.__title} | Capacity: {self.__capacity} | Booked Seats: {self.__booked_seats} | Status: {self.__status.value}")
    #Bonus A
    def reopen_show(self):
     if self.__status == ShowStatus.CANCELLED:
        raise ShowCancelledError(
            "Cancelled shows cannot be reopened."
        )

     if self.__status != ShowStatus.SOLD_OUT:
        raise InvalidStatusError(
            "Only sold-out shows can be reopened."
        )

     self.__status = ShowStatus.OPEN
class InvalidBookingError(Exception):
    pass

class ShowSoldOutError(Exception):
    pass
class ShowCancelledError(Exception):
    pass
class InvalidStatusError(Exception):
    pass

#Tests
print("Testing MovieShow class : Happy Path")
customer1 = Customer(
    "John Doe",
    "john@email.com",
    101
)

show = MovieShow(
    "Avengers",
    100,
    0,
    ShowStatus.OPEN
)

show.display_info()

try:
    print(show.book_tickets(customer1, 5))
except Exception as e:
    print(e)

show.display_info()

print("Invalid Booking Test")
try:
    show.book_tickets(customer1, 1000)
except InvalidBookingError as e:
    print("Booking Error:", e)
try:
    sold_out_show = MovieShow(
        "Batman",
        10,
        10,
        ShowStatus.SOLD_OUT
    )

    sold_out_show.book_tickets(customer1, 1)

except ShowSoldOutError as e:
    print("Sold Out Error:", e)
try:
    cancelled_show = MovieShow(
        "Superman",
        50,
        0,
        ShowStatus.CANCELLED
    )

    cancelled_show.book_tickets(customer1, 1)
except ShowCancelledError as e:
    print("Cancelled Show Error:", e)

try:
    show.status = "OPEN"

except InvalidStatusError as e:
    print("Status Error:", e) 