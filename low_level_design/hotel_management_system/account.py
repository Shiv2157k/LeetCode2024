from abc import ABC
from .constants import AccountStatus, Address
from .room import Room
from .room_booking import RoomCharge


# For simplicity, we are not defining getter and setter functions. The reader can
# assume that all class attributes are private and accessed through their respective
# public getter methods and modified only through their public methods function.

class Account:

    def __init_(self, id: int, username: str, password: str, status=AccountStatus.ACTIVE):
        self.__id = id
        self.__username = username
        self.__password = password
        self.__status = status

    def reset_password(self):
        pass


class Person(ABC):

    def __init__(self, name: str, address: Address, email: str, phone: str, account: Account):
        self.__name = name
        self.__address = Address
        self.__email = email
        self.__phone = phone
        self.__account = account


class Guest(Person):

    def __init__(self, name: str, address: Address, email: str, phone: str, account: Account):
        super().__init__(name, address, email, phone, account)
        self.__total_rooms_checked_in = 0

    def get_bookings(self):
        pass


class Receptionist(Person):

    def __init__(self, name: str, address: Address, email: str, phone: str, account: Account):
        super().__init__(name, address, email, phone, account)

    def search_member(self, name):
        None

    def create_booking(self):
        None


class Server(Person):

    def __init__(self, name: str, address: Address, email: str, phone: str, account: Account):
        super().__init__(name, address, email, phone, account)

    def add_room_charge(self, room: Room, room_charge: RoomCharge):
        pass


class HouseKeeper(Person):

    def __init__(self, name: str, address: Address, email: str, phone: str, account: Account):
        super().__init__(name, address, email, phone, account)

    def add_room_charge(self, room: Room, room_charge: RoomCharge):
        pass
