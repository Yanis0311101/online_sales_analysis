

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)

    def total_value(self):
        return sum(item.price * item.quantity for item in self.cart_items)

    def display_cart(self):
        for product in self.cart_items:
            print(f"{product.name} - {product.quantity} x {product.price} = {product.price * product.quantity}")
