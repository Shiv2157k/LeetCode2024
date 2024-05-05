from abc import ABC
from datetime import datetime

from .account import HouseKeeper
from .constants import RoomStyle, RoomStatus


class Search(ABC):

    def search(self, style: RoomStyle, start_date: datetime, duration: int):
        pass


class Room(Search):

    def __init__(self, room_number: int, room_style: RoomStyle, status: RoomStatus, price: float, is_smoking: bool):
        self.__room_number = room_number
        self.__room_style = room_style
        self.__status = status
        self.__price = price
        self._is_smoking = is_smoking

        self.__keys = []
        self.__house_keeping_log = []

    def is_room_available(self):
        return self.__status

    def check_int(self):
        pass

    def check_out(self):
        pass

    def search(self, style: RoomStyle, start_date: datetime, duration: int):
        pass
    # return all rooms with the given style and availability


class RoomKey:

    def __init__(self, key_id: int, barcode: str, is_active: bool, is_master: bool):
        self.__key_id = key_id
        self.__barcode = barcode
        self.__issued_at = datetime.today()
        self.__is_active = is_active
        self.__is_master = is_master

    def assign_room(self, room: Room):
        pass

    def is_active(self):
        pass


class RoomHouseKeeping:

    def __init__(self, description: str, duration: int, house_keeper: HouseKeeper):
        self.__description = description
        self.__start_datetime = datetime.today()
        self.__duration = duration
        self.__house_keeper = house_keeper

    def add_house_keeping(self, room: Room):
        pass
