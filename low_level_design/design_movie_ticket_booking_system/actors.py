from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, name, address, phone, email):
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__email = email


class Customer(Person):

    def __init__(self, name, address, phone, email):
        super().__init__(name, address, phone, email)
        self.__bookings = []

    def create_booking(self, booking):
        pass

    def update_booking(self, booking):
        pass

    def delete_booking(self, booking):
        pass


class Admin(Person):

    def __init__(self, name, address, phone, email):
        super().__init__(name, address, phone, email)

    def add_show(self, show):
        pass

    def update_show(self, show):
        pass

    def delete_show(self, show):
        pass

    def add_movie(self, movie):
        pass

    def delete_movie(self, movie):
        pass


class TicketAgent(Person):

    def __init__(self, name, address, phone, email):
        super().__init__(name, address, phone, email)

    def create_booking(self, booking):
        pass

    def view_booking(self, booking):
        pass
