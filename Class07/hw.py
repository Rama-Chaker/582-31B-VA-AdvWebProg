from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass


class Car(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
        return f"The {self.make} {self.model} is driving on the road."


class Bicycle(Vehicle):
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        return f"The {self.brand} bicycle is being pedaled on the path."


car = Car("Toyota", "Camry")
bicycle = Bicycle("Trek")
print(car.move())
print(bicycle.move())


class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


class TextFileHandler(FileHandler):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        return f"reading from {self.filename}"

    def write(self, data):
        return f"writing to {self.filename}: {data}"


class JsonFileHandler(FileHandler):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        return f"reading from {self.filename}"

    def write(self, data):
        return f"writing to {self.filename}: {data}"


text_handler = TextFileHandler("document.txt")
json_handler = JsonFileHandler("data.json")
print(text_handler.read())
print(text_handler.write("Hello, World!"))
print(json_handler.read())
print(json_handler.write('{"name": "Alice", "age": 30}'))


class Account(ABC):
    @abstractmethod
    def calculate_fee(self):
        pass


class SavingsAccount(Account):
    def __init__(self, balance):
        self.balance = balance

    def calculate_fee(self):
        return f"Monthly fee for Savings Account with balance ${self.balance}: ${self.balance * 0.01}"


class PremiumAccount(Account):
    def __init__(self, balance):
        self.balance = balance

    def calculate_fee(self):
        return f"Monthly fee for Premium Account with balance ${self.balance}: ${self.balance * 0.005}"


savings_account = SavingsAccount(1000)
print(savings_account.calculate_fee())
premium_account = PremiumAccount(1000)
print(premium_account.calculate_fee())


class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return f"Monthly salary for {self.name} (Full-Time): ${self.monthly_salary}"


class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return f"Monthly salary for {self.name} (Part-Time): ${self.hourly_rate * self.hours_worked}"


full_time_employee = FullTimeEmployee("Alice", 5000)
print(full_time_employee.calculate_salary())
part_time_employee = PartTimeEmployee("Bob", 20, 80)
print(part_time_employee.calculate_salary())


class Media(ABC):
    @abstractmethod
    def play(self):
        pass


class Song(Media):
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def play(self):
        return f"Playing song: '{self.title}' by {self.artist}."


class Video(Media):
    def __init__(self, title, director):
        self.title = title
        self.director = director

    def play(self):
        return f"Playing video: '{self.title}' directed by {self.director}."


song = Song("Shape of You", "Ed Sheeran")
video = Video("Bint El Hares", "Henry Barakat")
print(song.play())
print(video.play())
