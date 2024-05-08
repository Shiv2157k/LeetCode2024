from abc import ABC, abstractmethod
from .enumerations import AccountStatus
from .data_classes import Person
from datetime import datetime


class User(ABC):

    def __init__(self, id, password, person, card, status=AccountStatus.ACTIVE):
        self.__id = id
        self.__password = password
        self.__status = status
        self.__person = person
        self.__card = card

    @abstractmethod
    def reset_password(self):
        pass


class Librarian(User):

    def __init__(self, id, password, person: Person, card, status=AccountStatus.ACTIVE):
        super().__init__(id, password, person, card, status)

    def add_book_item(self, book_item):
        book_item.set_added_by(self)
        pass

    def block_member(self, member):
        None

    def unblock_member(self, member):
        pass

    def reset_password(self):
        pass


class Member(User):

    def __init__(self, id, password, person, card, status=AccountStatus.ACTIVE):
        super().__init__(id, password, person, status)
        self.__date_of_membership = datetime.today()
        self.__total_books_checked_out = 0

    def reserve_book_item(self, book_item):
        pass

    def increment_total_books_checked_out(self):
        pass

    def checkout_book_item(self, book_item):
        pass

    def check_for_fine(self, book_item_barcode):
        pass

    def return_book_item(self, book_item):
        pass

    def renew_book_item(self, book_item):
        pass

    def reset_password(self):
        pass