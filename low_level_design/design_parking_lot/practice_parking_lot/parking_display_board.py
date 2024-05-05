from low_level_design.design_parking_lot.practice_parking_lot.parking_spot import HandicappedSpot, LargeSpot, \
    CompactSpot, ElectricSpot, MotorbikeSpot


class ParkingDisplayBoard:

    def __init__(self, id: int = 1):
        self.__id = id
        self.__handicapped_free_spot: HandicappedSpot = None
        self.__compact_free_spot: CompactSpot = None
        self.__large_free_spot: LargeSpot = None
        self.__motorbike_free_spot: MotorbikeSpot = None
        self.__electric_free_spot: ElectricSpot = None

    def get_handicapped_free_spot(self):
        return self.__handicapped_free_spot

    def set_handicapped_free_spot(self, spot):
        self.__handicapped_free_spot.get_type(spot)

    def get_compact_free_spot(self):
        return self.__compact_free_spot

    def get_large_free_spot(self):
        return self.__large_free_spot

    def get_motorbike_free_spot(self):
        return self.__motorbike_free_spot

    def show_empty_spot_number(self):
        message: str = ""

        if self.__handicapped_free_spot.is_free():
            message += "Free Handicapped: " + self.__handicapped_free_spot.get_number()
        else:
            message += "Handicapped is full"
        message += "\n"

        if self.__compact_free_spot.is_free():
            message += "Free Compact: " + self.__compact_free_spot.get_number()
        else:
            message += "Compact is full"
        message += "\n"

        if self.__large_free_spot.is_free():
            message += "Free Large: " + self.__large_free_spot.get_number()
        else:
            message += "Large is full"
        message += "\n"

        if self.__motorbike_free_spot.is_free():
            message += "Free Motorbike: " + self.__motorbike_free_spot.get_number()
        else:
            message += "Motorbike is full"
        message += "\n"

        if self.__electric_free_spot.is_free():
            message += "Free Electric: " + self.__electric_free_spot.get_number()
        else:
            message += "Electric is full"

        print(message)
