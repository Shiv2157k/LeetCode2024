from typing import List
from .meeting_room import MeetingRoom
from .user import User
from .calendar import Calendar
from .interval import Interval


class __MeetingScheduler(object):
    __instances = None

    # Scheduler is a singleton class that ensures it will have only one active instance at a time
    def __new__(cls, __MeetingScheduler=None):
        if cls.__instances is None:
            cls.__instances = super(__MeetingScheduler, cls).__new__()
        return cls.__instances


class MeetingSchedule(metaclass=__MeetingScheduler):

    def __init__(self, organizer: User, calender: Calendar):
        self.__organizer = organizer
        self.__calender = calender
        self.__rooms: List[MeetingRoom] = []

    def schedule_meeting(self, users: List[User], interval: Interval):
        pass

    def cancel_meeting(self, users: User, interval: Interval):
        pass

    def book_room(self, room: MeetingRoom, number_of_persons: int, interval: Interval):
        pass

    def release_room(self, room: MeetingRoom, interval: Interval):
        pass

    def check_rooms_availability(self, number_of_persons: int, interval: Interval):
        pass
