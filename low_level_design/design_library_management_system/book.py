from abc import ABC, abstractmethod
from .data_classes import Person
from .user import Librarian


class Rack:

    def __init__(self, number, location_identifier):
        self.__number = number
        self.__location_identifier = location_identifier
        self.__book_items = []

    def add_book_item(self, book_item):
        pass


class Book(ABC):

    def __init__(self, isbn, title, subject, publisher, language, number_of_pages, book_format):
        self.__isbn = isbn
        self.__title = title
        self.__subject = subject
        self.__publisher = publisher
        self.__language = language
        self.__number_of_pages = number_of_pages
        self.__book_format = book_format
        self.__authors = []


    def add_authors(self, author: Person):
        pass


class BookItem(Book):

    def __init__(self, id, is_reference_only, borrowed, due_date, price, status, date_of_purchase, publication_date, placed_at: Rack):
        # calling parent class constructor
        super().__init__(None, None, None, None, 0, None)
        self.id = id
        self.is_reference_only = is_reference_only
        self.borrowed = borrowed
        self.due_date = due_date
        self.price = price
        self.status = status
        self.date_of_purchase = date_of_purchase
        self.publication_date = publication_date
        self.placed_at = placed_at
        self.book = None # composition: BookItem has a reference to a Book

    def checkout(self, member_if):
        # Implementation for checkout logic
        # Update the status, set due date, etc.
        # Return True if checkout is successful, False otherwise
        return True  # Placeholder, replace with actual logic

    def set_placed_at(self, rack: Rack):
        self.placed_at = rack

    def set_added_by(self, librarian: Librarian):
        # Implementation for setting the librarian who added the book item
        # This might involve updating logs or other data related to the librarian
        # No return value as it's a setter method
        pass

    # other methods

    def get_book(self):
        return self.book


