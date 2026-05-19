# Ex.1

# Create a class with:
#   name
#   private __gpa
# Requirements:
#   property gpa
#   setter only accepts values between 0.0 and 4.0


class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.__gpa = gpa

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value):
        if 0.0 <= value <= 4.0:
            self.__gpa = value
        else:
            print("Invalid GPA value")

st = Student("Alice", 3.5)
print("Your GPA is:", st.gpa)
st.gpa = 4.1
# Ex.2

# Create a class with:
#   name
#   internal _price
# Requirements:
#   property price

# setter must reject negative values

class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            print("Price cannot be negative")

p = Product("Laptop", 999.99)
print("Price:", p.price)
p.price = -899.99

# Ex.3 

# Create a class with:
#   radius

# Requirements:
# a read-only property area

# You should not store area directly; you should compute it.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        import math
        return math.pi * self.radius ** 2
c = Circle(5)
print("Area:", format(c.area, ".2f"))

# Ex.4 

# Create a class with:
#   first_name
#   last_name
# Requirements:
#   read-only property full_name

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

p = Person("John", "Doe")
print("Full Name:", p.full_name)
p.first_name = "Jane"
print("Full Name:", p.full_name)
# Ex.5

# Create a class with:
#   owner
#   private __balance
# Requirements:
#   property balance
#   setter prevents negative values
#   method deposit(amount)
#   method withdraw(amount)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            print("Balance cannot be negative")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount")
account = BankAccount("Alice", 500)
print("Initial Balance:", account.balance)
account.deposit(200)
print("Balance after deposit:", account.balance)
account.withdraw(100)
print("Balance after withdrawal:", account.balance)
account.balance = -50

# Ex.6

# Create a class with:
#   name
#   private __price
#   quantity
# Requirements:
#   property price
#   setter prevents negative values
#   read-only property inventory_value

class Food:
    def __init__(self, name, price, quantity):
        self.name = name
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value
        else:
            print("Price cannot be negative")

    @property
    def inventory_value(self):
        return self.__price * self.quantity
f = Food("Apple", 0.5, 100)
print("Price:", f.price)
print("Inventory Value:", f.inventory_value)
f.price = -0.5

# Ex.7

# Create a class with:
#   title
#   private __rating
# Requirements:
#   property rating
#   setter only accepts values between 0 and 10

class Series:
    def __init__(self, title, rating):
        self.title = title
        self.__rating = rating

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if 0 <= value <= 10:
            self.__rating = value
        else:
            print("Rating must be between 0 and 10")
s = Series("My Favorite Show", 8.5)
print("Rating:", s.rating)
s.rating = 11