from user import Customer, Staff

customer1 = Customer("John Doe", "john@email.com", 101)
staff1 = Staff("Alice Smith", "alice@email.com", 5001)

users = [customer1, staff1]

print("Polymorphism")

for user in users:
    user.display_info()
    print()
