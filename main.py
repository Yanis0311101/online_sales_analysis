

from src.product import Product
from src.product_manager import ProductManager


manager = ProductManager()


manager.add_product(Product("Laptop", 3500, 10))
manager.add_product(Product("Mouse", 100, 50))
manager.add_product(Product("Monitor", 800, 20))


manager.display_all_products()
manager.total_inventory_value()
