from enum import Enum


class Suit(Enum):
    HEART = 1
    SPADE = 2
    CLUB = 3
    DIAMOND = 4


class AccountStatus(Enum):
    ACTIVE = 1
    CLOSED = 2
    CANCELED = 3
    BLACKLISTED = 4
    NONE = 5


class Person:

    def __init__(self, name, street_address, city, state, zip_code, country):
        self.__name = name
        self.__street_address = street_address
        self.__city = city
        self.__zip_code = zip_code
        self.__country = country
