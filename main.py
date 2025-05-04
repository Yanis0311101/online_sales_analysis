

from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()


product1 = Product("Laptop", 3500, 5)
product2 = Product("Telefon", 1500, 10)
product3 = Product("Căști", 300, 15)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)

cart = Cart()


cart.add_to_cart(product1)
cart.add_to_cart(product2)


cart.display_cart()
print(f"Total de plată: {cart.total_value()} RON")
