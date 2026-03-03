"""
Shopping Cart: OOP for Online Stores
Scenario:
Simulate adding/removing items and computing the bill in an online store.

What you’ll learn:
Real-world application of classes
Encapsulation and methods

Task:
Design a ShoppingCart class with add, remove, and total methods.

Example:
Add "Book" (2 × 200) and "Pen" (5 × 20); show total.

http://192.168.2.101/link/421#bkmrk-expected-output%3A-16
 
Expected Output:
500
"""
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add(self, name, quantity, price):
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"quantity": quantity, "price": price}

    def remove(self, name):
        if name in self.items:
            del self.items[name]

    def total(self):
        total_amount = 0
        for item in self.items.values():
            total_amount += item["quantity"] * item["price"]
        return total_amount


cart = ShoppingCart()

cart.add("Book", 2, 200)
cart.add("Pen", 5, 20)

print(cart.total())
