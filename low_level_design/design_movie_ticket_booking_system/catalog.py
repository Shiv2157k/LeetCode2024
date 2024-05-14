from abc import ABC, abstractmethod


class Search(ABC):

    @abstractmethod
    def search_by_movie_title(self, title):
        pass

    @abstractmethod
    def search_movie_by_language(self, language):
        pass

    @abstractmethod
    def search_movie_by_genre(self, genre):
        pass

    @abstractmethod
    def search_movie_by_release_date(self, date):
        pass


class Catalog(Search):

    def __init__(self):
        self.__movie_titles = {}
        self.__movie_languages = {}
        self.__movie_genres = {}
        self.__movie_release_dates = {}

    def search_movie_by_language(self, language):
        pass

    def search_movie_by_release_date(self, date):
        pass

    def search_by_movie_title(self, title):
        pass

    def search_movie_by_genre(self, genre):
        pass

