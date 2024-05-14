from abc import ABC, abstractmethod


class Search(ABC):
    def search_products_by_name(self, name):  # Returns list of product names
        pass

    def search_products_by_category(self, category):  # Returns list of product categories
        pass


class Catalog(Search):
    def __init__(self):
        self.__products = {}

    # Returns list of product names
    def search_products_by_name(self, name):
        # functionality
        pass

    # Returns list of product categories
    def search_products_by_category(self, category):
        # functionality
        pass
