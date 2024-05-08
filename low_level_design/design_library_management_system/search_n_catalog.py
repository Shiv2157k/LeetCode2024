from abc import ABC, abstractmethod


class Search(ABC):

    @abstractmethod
    def search_by_title(self, title):
        pass

    @abstractmethod
    def search_by_author(self, author):
        pass

    @abstractmethod
    def search_by_subject(self, subject):
        pass

    @abstractmethod
    def search_by_publication_date(self, publish_date):
        pass


class Catalog(Search):

    def __init__(self):
        self.__book_titles = {}
        self.__book_authors = {}
        self.__book_subjects = {}
        self.__book_publication_dates = {}

    def search_by_publication_date(self, publish_date):
        pass

    def search_by_author(self, author):
        pass

    def search_by_title(self, title):
        pass

    def search_by_subject(self, subject):
        pass
