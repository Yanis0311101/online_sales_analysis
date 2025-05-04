

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_product(self, product):
        self.cart_items.append(product)

    def calculate_total(self):
        return sum(item.price * item.quantity for item in self.cart_items)

    def display_cart(self):
        for item in self.cart_items:
            print(f"{item.name} - {item.quantity} x {item.price} RON")
        print(f"Total: {self.calculate_total()} RON")
