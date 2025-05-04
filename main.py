from product import Product
from product_manager import ProductManager
from cart import Cart


product_manager = ProductManager()


product_manager.add_product(Product("Laptop", 3000, 5))
product_manager.add_product(Product("Telefon", 1500, 10))
product_manager.add_product(Product("Căști", 200, 15))


cart = Cart()


import random
for _ in range(3):
    product = random.choice(product_manager.products)
    cart.add_product(product)


cart.display_cart()


