from typing import List
from .interval import Interval
from .meeting_room import MeetingRoom
from .user import User


class Meeting:

    def __init__(self, id: int, participants_count: int, interval: Interval, room: MeetingRoom, subject: str):
        self.__id = id
        self.__participants_count = participants_count
        self.__participants: List[User] = []
        self.__interval = interval
        self.__room = room
        self.__subject = subject

    def add_participant(self, participants: List[User]):
        pass
