"""
A shop needs an iterable object to keep track of product expiration dates.
Each product in the shop will have a string name, datetime expiration date and quantity
Iterating the object will return all products in the shop ordered by expiration date
1) 40p: Definition
    a) 10p: Basic class structure of objects
    b) 10p: Basic class structure of iterator
    b) 10p: Method to add product to the shop
    c) 10p: Method to decrease quantity and remove product
2) 40p: Execution:
    a) 10p: Create instance of your shop
    b) 10p: Add products:
        - Banana, 1 Aug 2022, 100
        - Orange, 2 Aug 2022, 200
        - Orange, 3 Aug 2022, 50
    c) 10p: Remove products
        - Orange, 10
        - Banana, 50
    d) 10p: Iterate the created object.
3) 20p: Documenting:
   a) 5p: type hints for arguments
   a) 5p: module documentation
   b) 5p: class documentation for all classes
   c) 5p: method documentation for all methods
"""

import time
import datetime


class expirationDate_Tracker:
    """something"""

    products = {}

    def __init__(self, day: float):
        self.day = datetime.datetime.now()

    def __iter__(self):
        return ProductIterator(self.products)

    def add_quantity(self, name, quantity):
        """something"""

        self.products[name] = [int(quantity)]

    def add_expiration_date(self, name, expiration_date):
        day, month, year = expiration_date.split(" ")
        self.products[name].append((int(day), month, int(year)))
        print(self.products[name])

    def remove_Product(self, name, quantity):
        self.products[name][0] = self.products[name][0] - int(quantity)


class ProductIterator():
    all_products = []

    def __init__(self, products: dict):
        self.products = products
        for product_name, info in self.products.items():
            print(product_name, info)
            # self.all_products.append((name, day, month, year, quantity))

    def __iter__(self):
        return self

    def __next__(self):
        if not self.all_products:
            raise StopIteration
        return self.all_products.pop()


k = expirationDate_Tracker(time.time())
k.add_quantity('Banana', "100")
k.add_expiration_date('Banana', "1 Aug 2022")

k.add_quantity('Orange', "100")
k.add_expiration_date('Orange', "2 Aug 2022")

k.add_quantity('Orange', "50")
k.add_expiration_date('Orange', "3 Aug 2022")

k.remove_Product('Orange', '10')
k.remove_Product('Banana', '50')

for emp in k:
    print(emp)
