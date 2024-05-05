from constants import ParkingSpotType
from low_level_design.design_parking_lot.practice_parking_lot.parking_spot import ParkingSpot
from low_level_design.design_parking_lot.practice_parking_lot.vehicle import Vehicle
from parking_display_board import ParkingDisplayBoard


class ParkingFloor:

    def __init__(self, name: str):
        self.__name = name
        self.__handicapped_spots = {}
        self.__compact_spots = {}
        self.__large_spots = {}
        self.__motorbike_spots = {}
        self.__electric_spots = {}
        self.__info_portals = {}
        self.__free_handicapped_spot_count = {"free_spot": 0}
        self.__free_compact_spot_count = {"free_spot": 0}
        self.__free_large_spot_count = {"free_spot": 0}
        self.__free_motorbike_spot_count = {"free_spot": 0}
        self.__free_electric_spot_count = {"free_spot": 0}
        self.__display_board = ParkingDisplayBoard()

    def add_parking_spot(self, spot: ParkingSpot):
        switcher = {
            ParkingSpotType.HANDICAPPED:
                self.__handicapped_spots.get(spot.get_number(), spot),
            ParkingSpotType.COMPACT:
                self.__compact_spots.get(spot.get_number(), spot),
            ParkingSpotType.LARGE:
                self.__large_spots.get(spot.get_number(), spot),
            ParkingSpotType.ELECTRIC:
                self.__electric_spots.get(spot.get_number(), spot),
            ParkingSpotType.MOTORBIKE:
                self.__motorbike_spots.get(spot.get_number(), spot)
        }
        switcher.get(spot.get_type(), "Wrong Parking Spot Type")

    def assign_vehicle_to_spot(self, vehicle: Vehicle, spot: ParkingSpot):
        spot.assign_vehicle(vehicle)
        switcher = {
            ParkingSpotType.HANDICAPPED: self.update_display_board_for_handicapped(spot),
            ParkingSpotType.MOTORBIKE: self.update_display_board_for_motorbike(spot)
        }
        switcher(spot.get_number(), "Wrong parking spot type!")

    def update_display_board_for_handicapped(self, spot: ParkingSpot):
        if self.__display_board.get_handicapped_free_spot().get_number() == spot.get_number():
            # find another free handicapped parking and assign to display board
            for key in self.__handicapped_spots:
                if self.__handicapped_spots.get(key).is_free():
                    self.__display_board.set_handicapped_free_spot(self.__handicapped_spots.get(key))
            self.__display_board.show_empty_spot_number()

    def update_display_board_for_compact(self, spot: ParkingSpot):
        pass

    def update_display_board_for_large(self, spot: ParkingSpot):
        pass

    def update_display_board_for_electric(self, spot: ParkingSpot):
        pass

    def update_display_board_for_motorbike(self, spot: ParkingSpot):
        pass

    def free_spot(self, spot: ParkingSpot):
        spot.remove_vehicle()
        switcher = {
            ParkingSpotType.HANDICAPPED: self.__free_handicapped_spot_count.update(
                free_spot=self.__free_compact_spot_count["free_spot"] + 1
            ),
            ParkingSpotType.COMPACT: self.__free_compact_spot_count.update(
                free_spot=self.__free_compact_spot_count["free_spot"] + 1
            ),
            ParkingSpotType.LARGE: self.__free_large_spot_count.update(
                free_spot=self.__free_large_spot_count["free_spot"] + 1
            ),
            ParkingSpotType.MOTORBIKE: self.__free_motorbike_spot_count.update(
                free_spot=self.__free_motorbike_spot_count["free_spot"] + 1
            ),
            ParkingSpotType.ELECTRIC: self.__free_electric_spot_count.update(
                free_spot=self.__free_electric_spot_count["free_spot"] + 1
            )
        }
        switcher(spot.get_type(), "Wrong parking spot type!")
