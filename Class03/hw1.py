class Playlist:
    def __init__(self, name, song_count):
        self.name = name
        self.song_count = song_count

    def add_song(self):
        self.song_count += 1

    def remove_song(self):
        if self.song_count > 0:
            self.song_count -= 1
        else:
            print("Song count is invalid.")

    def show_info(self):
        print(f"Playlist: {self.name}, Song Count: {self.song_count}")


playlist1 = Playlist("My Favorite Songs", 10)
playlist1.add_song()
playlist1.show_info()
playlist1.remove_song()
playlist1.show_info()


class ShoppingCart:
    def __init__(self, owner, item_count):
        self.owner = owner
        self.item_count = item_count

    def add_item(self, quantity):
        self.item_count += quantity

    def remove_item(self, quantity):
        if self.item_count >= quantity:
            self.item_count -= quantity
        else:
            print("Item not found in the cart.")

    def show_cart(self):
        print(f"Shopping Cart for {self.owner}:")
        print(f"Item Count: {self.item_count}")


cart1 = ShoppingCart("Alice", 5)
cart1.add_item(3)
cart1.show_cart()
cart1.remove_item(2)
cart1.show_cart()


class UserAccount:
    def __init__(self, username, active, login_count):
        self.username = username
        self.active = active
        self.login_count = login_count

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def login(self):
        if self.active:
            self.login_count += 1
        else:
            print("Account is inactive. Please activate your account to login.")

    def show_status(self):
        print(f"Username: {self.username}, Active: {self.active}")


user1 = UserAccount("john_doe", False, 0)
user1.activate()
user1.login()
user1.show_status()
user1.deactivate()
user1.login()
