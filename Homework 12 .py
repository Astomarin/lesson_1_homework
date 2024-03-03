class Item:
    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"{self.name}: {self.price} pcs."


class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        items_str = "\n".join([f"{item.name}: {count} pcs." for item, count in self.products.items()])
        return f"User: {self.user}\nItems:\n{items_str}"

    def get_total(self):
        self.total = sum(item.price * count for item, count in self.products.items())
        return self.total


lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")
print(lemon)  # lemon: 5 pcs.
print(apple)  # apple: 2 pcs.
buyer1 = User("Ivan", "Ivanov", "02628162")
print(buyer1)  # Ivan Ivanov
buyer2 = User("Alex", "Hillel", "041232123")

cart1 = Purchase(buyer1)
cart2 = Purchase(buyer2)

cart1.add_item(lemon, 4)
cart1.add_item(apple, 20)
cart2.add_item(lemon, 14)
cart2.add_item(apple, 25)
print(cart1)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""
print(cart2)

assert isinstance(cart1.user, User) is True, 'Екземпляр класу User'
assert cart1.get_total() == 60, "Всього 60"
assert cart1.get_total() == 60, 'Повинно залишатися 60!'
## Для другого юзера
assert isinstance(cart2.user, User) is True, 'Екземпляр класу User'
assert cart2.get_total() == 120, "Всього 120"
assert cart2.get_total() == 120, 'Повинно залишатися 120!'
cart1.add_item(apple, 10)
cart2.add_item(apple, 5)
print(cart1)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""
print(cart2)
assert cart1.get_total() == 40
assert cart2.get_total() == 80
