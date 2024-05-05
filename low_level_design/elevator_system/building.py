from .door_floor import Floor
from typing import List
from .elevator_car import ElevatorCar


class __Building(object):
    __instances = None

    def __new__(cls):
        if cls.__instances is None:
            cls.__instances = super(cls).__new__(cls)
        return cls.__instances


class Building(metaclass=__Building):

    def __init__(self):
        self.__floor: List[Floor] = []
        self.__elevator: List[ElevatorCar] = []
