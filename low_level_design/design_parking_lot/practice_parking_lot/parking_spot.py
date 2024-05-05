from abc import ABC
from constants import ParkingSpotType
from low_level_design.design_parking_lot.practice_parking_lot.vehicle import Vehicle


class ParkingSpot(ABC):

    def __init__(self, number: int, parking_spot_type: ParkingSpotType):
        self.__number = number
        self.__free = True
        self.__vehicle = None
        self.__parking_spot_type = parking_spot_type

    def get_number(self):
        return self.__number

    def is_free(self):
        return self.__free

    def get_type(self):
        return self.__parking_spot_type

    def assign_vehicle(self, vehicle: Vehicle):
        self.__vehicle = vehicle
        self.__free = True

    def remove_vehicle(self):
        self.__vehicle = None
        self.__free = False


class HandicappedSpot(ParkingSpot):

    def __init__(self, number):
        super().__init__(number, ParkingSpotType.HANDICAPPED)


class CompactSpot(ParkingSpot):

    def __init__(self, number):
        super().__init__(number, ParkingSpotType.COMPACT)


class LargeSpot(ParkingSpot):

    def __init__(self, number):
        super().__init__(number, ParkingSpotType.LARGE)


class MotorbikeSpot(ParkingSpot):

    def __init__(self, number):
        super().__init__(number, ParkingSpotType.MOTORBIKE)


class ElectricSpot(ParkingSpot):

    def __init__(self, number):
        super().__init__(number, ParkingSpotType.ELECTRIC)
