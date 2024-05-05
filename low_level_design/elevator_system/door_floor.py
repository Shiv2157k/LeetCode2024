from .constants import DoorState
from .display import Display
from .panels import HallPanel


class Door:

    def __init__(self, state: DoorState):
        self.__state = state

    def is_open(self):
        pass


class Floor:

    def __init__(self, display: Display, panel: HallPanel):
        self.__display = display
        self.__panel = panel

    def is_bottom_most(self):
        None

    def is_top_most(self):
        None
