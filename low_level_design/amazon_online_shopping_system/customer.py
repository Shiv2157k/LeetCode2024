from abc import ABC, abstractmethod


class Customer(ABC):

    def __init__(self, cart, order):
        self.__cart = cart # shopping cart class isntance


    @abstractmethod
    def get_shopping_cart(self):
        pass


class Guest(Customer):

    def __init__(self, cart, order):
        super().__init__(cart, order)


    def register_account(self):
        pass

    def get_shopping_cart(self):
        pass


class AuthenticatedUser(Customer):

    def __init__(self, account, card, order):
        self.__account = account
        self.__order = order
        super().__init__(card, order)

    def place_order(self, order):
        pass

    def get_shopping_cart(self):
        pass