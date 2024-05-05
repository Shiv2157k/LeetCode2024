from enum import Enum


class ParkingSpotType(Enum):
    COMPACT = 1
    LARGE = 2
    MOTORBIKE = 3
    HANDICAPPED = 4
    ELECTRIC = 5


class VehicleType(Enum):
    CAR = 1
    TRUCK = 2
    VAN = 3
    ELECTRIC = 4
    MOTORBIKE = 5


class ParkingTicketStatus:
    ACTIVE = 1
    PAID = 2
    LOST = 3


class AccountStatus(Enum):
    ACTIVE = 1
    COMPROMISED = 2
    BLOCKED = 3
    BANNED = 4
    ARCHIVED = 5
    UNKNOWN = 6


class Address:

    def __init__(self, street: str, city: str, state: str, zipcode: int, country: str):
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zipcode = zipcode
        self.__country = country


class Person:

    def __init__(self, name: str, address: Address, email: str, phone: str):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
