
from src.product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_all_products(self):
        print("Produsele disponibile:")
        for product in self.products:
            product.display_info()

    def total_inventory_value(self):
        total = sum(p.price * p.quantity for p in self.products)
        print(f"Valoarea totală a inventarului: {total} RON")
        return total
