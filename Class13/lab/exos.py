# 1
# Create a parent class:

#   Animal
#   method: speak()
class Animal:
    def speak(self):
        pass
# then child classes:
#   Dog
#   Cat
class Dog(Animal):
    def speak(self):
        return "Woof"
class Cat(Animal):
    def speak(self):
        return "Meow"
# Override speak in each child!

# Dog says "Woof"
# Cat says "Meow"

# Then loop through them polymorphically
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())

# 2
# Create a parent class: Vehicle
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def describe(self):
        return f"This is a {self.brand} vehicle."
# Child classes Car and Bike
class Car(Vehicle):
    def describe(self):
        return f"This is a {self.brand} car."
    def open_trunk(self):
        return "Trunk is now open."

class Bike(Vehicle):
    def describe(self):
        return f"This is a {self.brand} bike."
    def kickstand(self):
        return "Kickstand is down."

# they share 
# brand
# describe()
car = Car("Toyota")
bike = Bike("Yamaha")
print(car.describe())  
print(bike.describe()) 
print(car.open_trunk())  
print(bike.kickstand())  

# add child-specific behaviour

# 3
# parent class: Account
#               show_type()
class Account:
    def __init__(self, account_type):
        self.account_type = account_type
    def show_type(self):
        return f"This is a {self.account_type} account."
# children accounts: SavingsAccount & PremiumAccount
#   override or extend behaviour accordingly
class SavingsAccount(Account):
    def __init__(self):
        super().__init__("Savings")
    def calculate_interest(self, balance):
        return balance * 0.02
class PremiumAccount(Account):
    def __init__(self):
        super().__init__("Premium")
    def calculate_interest(self, balance):
        return balance * 0.05
savings = SavingsAccount()
premium = PremiumAccount()
print(savings.show_type())  
print(premium.show_type())  
print(f"Savings interest on $1000: ${savings.calculate_interest(1000)}") 
print(f"Premium interest on $1000: ${premium.calculate_interest(1000)}")