

class CartItem:

    def __init__(self, quantity, price):
        self.__quantity = quantity
        self.__price = price


    def update_quantity(self, quantity):
        pass


class ShoppingCart:

    def __init__(self, total_price, items):
        self.__total_price = total_price
        self.__items = items

    def add_item(self, item):
        pass

    def remove_item(self, item):
        pass

    def get_items(self):
        pass

    def checkout(self):
        pass