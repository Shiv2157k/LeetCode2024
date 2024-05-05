from low_level_design.design_parking_lot.parking_lot_enums import ParkingSpotType
from low_level_design.design_parking_lot.ParkingSpot import ParkingSpot, \
    HandicappedSpot, CompactSpot, LargeSpot, ElectricSpot, MotorBikeSpot


class ParkingFloor:

    def __init__(self, name):
        self.__name = name
        self.__handicapped_spots = {}
        self.__compact_spots = {}
        self.__large_spots = {}
        self.__motorbike_spots = {}
        self.__electric_spots = {}
        self.__info_portals = {}
        self.__free_handicapped_spot_count = {'free_spot': 0}
        self.__free_compact_spot_count = {'free_spot': 0}
        self.__free_large_spot_count = {'free_spot': 0}
        self.__free_motorbike_spot_count = {'free_spot': 0}
        self.__free_electric_spot_count = {'free_spot': 0}
        self.__display_board = ParkingDisplayBoard()

    def add_parking_spot(self, spot: ParkingSpot):
        switcher = {
            ParkingSpotType.HANDICAPPED:
                self.__handicapped_spots.get(spot.get_number(), spot),
            ParkingSpotType.COMPACT:
                self.__compact_spots.get(spot.get_number(), spot),
            ParkingSpotType.LARGE:
                self.__large_spots.get(spot.get_number(), spot),
            ParkingSpotType.MOTORBIKE:
                self.__motorbike_spots.get(spot.get_number(), spot),
            ParkingSpotType.ELECTRIC:
                self.__electric_spots.get(spot.get_number(), spot),
        }
        switcher.get(spot.get_type(), 'Wrong Parking Spot Type')

    def assign_vehicle_to_spot(self, vehicle, spot: ParkingSpot):
        spot.assign_vehicle(vehicle)
        switcher = {
            ParkingSpotType.HANDICAPPED:
                self.__display_board.get(spot),
            ParkingSpotType.COMPACT:
                self.__display_board.get(spot),
            ParkingSpotType.LARGE:
                self.__display_board.get(spot),
            ParkingSpotType.MOTORBIKE:
                self.__display_board.get(spot),
            ParkingSpotType.ELECTRIC:
                self.__display_board.get(spot),
        }

    def update_display_board_for_handicapped(self, spot):
        if self.__display_board.get_handicapped_free_spot().get_number() == spot.get_number():
            # find another free handicapped parking and assign to dispaly board
            for key in self.__handicapped_spots:
                if self.__handicapped_spots.get(key).is_free():
                    self.__display_board.set_handicapped_free_spot(self.__handicapped_spots.get(key))
            self.__display_board.show_empty_spot_number()

    def update_display_board_for_compact(self, spot):
        if self.__display_board.get_handicapped_free_spot().get_number() == spot.get_number():
            # find another free handicapped parking and assign to dispaly board
            for key in self.__handicapped_spots:
                if self.__handicapped_spots.get(key).is_free():
                    self.__display_board.set_handicapped_free_spot(self.__handicapped_spots.get(key))
            self.__display_board.show_empty_spot_number()

    def free_spot(self, spot: ParkingSpot):
        spot.remove_vehicle()
        switcher = {
            ParkingSpotType.HANDICAPPED:
                self.__free_handicapped_spot_count.update(
                    free_spot=self.__free_handicapped_spot_count["free_spot"] + 1
                ),
            ParkingSpotType.LARGE:
                self.__free_large_spot_count.update(
                    free_spot=self.__free_large_spot_count["free_spot"] + 1
                ),
            ParkingSpotType.COMPACT:
                self.__free_compact_spot_count.update(
                    free_spot=self.__free_compact_spot_count["free_spot"] + 1
                ),
            ParkingSpotType.MOTORBIKE:
                self.__free_motorbike_spot_count.update(
                    free_spot=self.__free_motorbike_spot_count["free_spot"] + 1
                ),
            ParkingSpotType.ELECTRIC:
                self.__free_electric_spot_count.update(
                    free_spot=self.__free_electric_spot_count["free_spot"] + 1
                )
        }
        switcher(spot.get_type(), "Wrong parking spot type")


class ParkingDisplayBoard:

    def __init__(self, id):
        self.__id = id
        self.__handicapped_free_spot: HandicappedSpot = None
        self.__compact_free_spot: CompactSpot = None
        self.__large_free_spot: LargeSpot = None
        self.__motorbike_free_spot: MotorBikeSpot = None
        self.__electric_free_spot: ElectricSpot = None

    def get_handicapped_free_spot(self):
        return self.__handicapped_free_spot

    def set_handicapped_free_spot(self, key, value):
        self.__handicapped_free_spot[key] = value

    def get_compact_free_spot(self):
        return self.__compact_free_spot

    def get_large_free_spot(self):
        return self.__large_free_spot

    def get_motorbike_free_spot(self):
        return self.__motorbike_free_spot

    def get_electric_free_spot(self):
        return self.__electric_free_spot

    def show_empty_spot_number(self):

        message = ""
        if self.__handicapped_free_spot.is_free():
            message += "Free Handicapped: " + self.__handicapped_free_spot.get_number()
        else:
            message += "Handicapped is Full"
        message += "\n"

        if self.__compact_free_spot.is_free():
            message += "Free Compact: " + self.__compact_free_spot.get_number()
        else:
            message += "Compact is Full"
        message += "\n"

        if self.__large_free_spot.is_free():
            message += "Free Large: " + self.__large_free_spot.get_number()
        else:
            message += "Large is Full"
        message += "\n"

        if self.__motorbike_free_spot.is_free():
            message += "Free MotorBike: " + self.__motorbike_free_spot.get_number()
        else:
            message += "MotorBike is Full"
        message += "\n"

        if self.__electric_free_spot.is_free():
            message += "Free Electric: " + self.__electric_free_spot.get_number()
        else:
            message += "Electric is Full"
        message += "\n"
