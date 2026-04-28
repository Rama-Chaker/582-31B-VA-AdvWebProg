class Fruit:
    def __init__(self, name, price, flavor):
        self.name = name
        self.price = price
        self.flavor = flavor

    def fruit_name(self):
        return self.name

    def fruit_price(self):
        return self.price

    def fruit_flavor(self):
        return self.flavor
    
    def new_price(self, price):
        self.price = price
        return self.price

fruit1 = Fruit("Apple", 0.99, "Sweet")
print(fruit1.fruit_name())
print(fruit1.fruit_price())
print(fruit1.fruit_flavor())
fruit1.new_price(0.89)
print(fruit1.fruit_price())