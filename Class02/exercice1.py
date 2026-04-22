class Friend:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age
    def print_info(self):
            print(self.name, self.last_name, self.age)
            
    def greet(self):
            print("Hello my name is", self.name)


friend1 = Friend("Alice", "Smith", 25)
friend2 = Friend("Bob", "Johnson", 30)
friend3 = Friend("Charlie", "Brown", 35)
friend1.greet()
friend2.greet()
friend3.greet()