from .constants import Address

class HotelLocation:

    def __init_(self, name: str, address: Address):
        self.__name = name
        self.__address = Address

    def get_rooms(self):
        None


class Hotel:

    def __init__(self, name):
        self.__name = name
        self.__locations = []

    def add_location(self, location: HotelLocation):
        self.__locations.append(location)