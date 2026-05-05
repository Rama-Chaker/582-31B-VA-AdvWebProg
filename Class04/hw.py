class Book:
    counter = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.counter += 1


book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")
print(f"Number of books created: {Book.counter}")
print(f"********** END OF EXERCISE 1 **********")


class Student:
    school_name = "Vanier College"
    student_count = 0

    def __init__(self, name, program, grade):
        self.name = name
        self.program = program
        self.grade = grade
        Student.student_count += 1

    def display_info(self):
        print(
            f"{self.name} studies {self.program} at {self.school_name}. Grade : {self.grade}"
        )


student1 = Student("Alice", "Computer Science", 85)
student2 = Student("Bob", "Mathematics", 90)
student3 = Student("Charlie", "Physics", 88)
student1.display_info()
student2.display_info()
student3.display_info()
print(f"Number of students created: {Student.student_count}")
print(f"********** END OF EXERCISE 2 **********")


class Product:
    category = "Electronics"
    tax_rate = 0.15

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def price_with_tax(self):
        return self.price + (self.price * self.tax_rate)


product1 = Product("Laptop", 1000)
product2 = Product("Smartphone", 500)
product3 = Product("Headphones", 200)
print(f"{product1.name} price with tax: ${product1.price_with_tax()}")
print(f"{product2.name} price with tax: ${product2.price_with_tax()}")
print(f"{product3.name} price with tax: ${product3.price_with_tax()}")
Product.tax_rate = 0.20
print(f"{product1.name} price with new tax rate: ${product1.price_with_tax()}")
print(f"{product2.name} price with new tax rate: ${product2.price_with_tax()}")
print(f"{product3.name} price with new tax rate: ${product3.price_with_tax()}")
print(f"********** END OF EXERCISE 3 **********")


class Employee:
    company_name = "TechNova"
    bonus_rate = 0.10
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.employee_count += 1

    def calculate_bonus(self):
        return self.salary * self.bonus_rate

    def display_employee(self):
        print(
            f"{self.name} works at {self.company_name}. Salary:  ${self.salary}. Bonus: ${self.calculate_bonus()}"
        )


employee1 = Employee("David", 60000)
employee2 = Employee("Emma", 75000)
employee3 = Employee("Frank", 50000)
print(f"********** 1st Display **********")
employee1.display_employee()
employee2.display_employee()
employee3.display_employee()
Employee.bonus_rate = 0.20
print(f"********** 2nd Display (after changing company bonus rate) **********")
employee1.display_employee()
employee2.display_employee()
employee3.display_employee()
employee1.bonus_rate = 0.50
print(f"********** 3rd Display (after changing individual bonus rate) **********")
employee1.display_employee()
employee2.display_employee()
employee3.display_employee()
Employee.bonus_rate = 0.05
print(f"********** 4th Display (after changing company bonus rate) **********")
employee1.display_employee()
employee2.display_employee()
employee3.display_employee()

# the 1st employee has a shadowed bonus rate , 
# because we assigned a new value to the bonus rate for employee1 , so we are using this new value instead of the class variable for employee1, 
# while employee2 and employee3 are still using the class variable for bonus rate.