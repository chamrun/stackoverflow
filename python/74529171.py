from dataclasses import dataclass


@dataclass
class Product:
    name: str
    quantity: int
    price: float


class Transaction:

    def __init__(self):
        self.products = {}

    def add_item(self, name, quantity, price):
        product_exists = self.product_exists(name)
        if product_exists:
            return False  # or raise Exception('Product already exists')
        else:
            self.products[name] = Product(name, quantity, price)
            return True

    def product_exists(self, name):
        return name in self.products.keys()


if __name__ == '__main__':
    t = Transaction()
    t.add_item("apple", 10, 1.5)
    t.add_item("banana", 20, 2.5)
    t.add_item("orange", 30, 3.5)
    print(t.products)
    print(t.product_exists("apple"))
    print(t.product_exists("pineapple"))

# You can return `True` or `False` in `check_if_not_exists` method.
# I suggest you to use `set` instead of `list` for `mapVal` attribute, because it's faster to check if an element exists in a `set` than in a `list`.
# I suggest you to rename your variables. `mapDict` and `mapVal` are not good names, instead you can use `products` and `product_names` or something like that.
# I suggest you to rename your methods. `add_item` and `check_if_not_exists` are not good names, instead you can use `add_product` and `product_exists` or something like that.


# You can remove product_names attribute and use products.keys() instead, and set product names as keys in products dictionary.