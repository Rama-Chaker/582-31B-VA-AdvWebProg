class Product:
    
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    @classmethod
    def one_comma_separated_string(cls, data):
        name, price, category = data.split(",")
        return cls(name, int(price), category)

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["price"], data["category"])

    @classmethod
    def just_name(cls, name):
        return cls(name, 0, "Unknown")
product1 = Product.one_comma_separated_string("Laptop,1000,Electronics")
product2 = Product.from_dict({"name": "Phone", "price": 500, "category": "Electronics"})
product3 = Product.just_name("Tablet")
product4 = Product.just_name("Headphones")
print(f"{product1.name} costs {product1.price} and belongs to {product1.category}")
print(f"{product2.name} costs {product2.price} and belongs to {product2.category}")
print(f"{product3.name} costs {product3.price} and belongs to {product3.category}")
print(f"{product4.name} costs {product4.price} and belongs to {product4.category}")