from typing import List
from .interval import Interval


class MeetingRoom:

    def __init__(self, id: int, capacity: int, is_available: bool):
        self.__id = id
        self.__capacity = capacity
        self.__is_available = is_available
        self.__booked_intervals: List[Interval]= []