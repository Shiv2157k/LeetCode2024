from abc import ABC

from low_level_design.design_parking_lot.parking_lot_enums import ParkingSpotType


class ParkingSpot(ABC):

    def __init__(self, number, parking_spot_type: ParkingSpotType):
        self.__number = number
        self.__free = True
        self.__vehicle = None
        self.__parking_spot_type = parking_spot_type

        # Getter method for the private field __number
    def get_number(self):
        return self.__number

    def get_type(self):
        return self.__parking_spot_type

    def is_free(self):
        return self.__free

    def assign_vehicle(self, vehicle):
        self.__vehicle = vehicle
        self.__free = False

    def remove_vehicle(self):
        self.__vehicle = None
        self.__free = True


class HandicappedSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.HANDICAPPED)


class CompactSpot(ParkingSpot):

    def __init__(self, number):
        super().__init__(number, ParkingSpotType.COMPACT)


class LargeSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.LARGE)


class ElectricSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.ELECTRIC)


class MotorBikeSpot(ParkingSpot):

    def __init__(self, number):
        super().__init__(number, ParkingSpotType.MOTORBIKE)
