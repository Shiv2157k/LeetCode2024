import threading

from low_level_design.design_parking_lot.parking_lot_enums import VehicleType


class ParkingLot:
    # singleton ParkingLot to ensure only one object of ParkingLot in the system,
    # all entrance panels will use this object to create new parking ticket: get_new_parking_ticket(),
    # similarly exit panels will also use this object to close parking tickets
    instance = None

    class __OnlyOne:

        def __init__(self, name, address):
            # 1. initialize variables: read name, address and parking_rate from database
            # 2. initialize parking floors: read the parking floor map from database,
            #    this map should tell how many parking spots are there on each floor. This
            #    should also initialize max spot counts too.
            # 3. initialize parking spot counts by reading all active tickets from database
            # 4. initialize entrance and exit panels: read from database
            self.__name = name
            self.__address = address
            self.__parking_rate = ParkingRate()

            self.__compact_spot_count = 0
            self.__large_spot_count = 0
            self.__motorbike_spot_count = 0
            self.__electric_spot_count = 0
            self.__max_compact_spot_count = 0
            self.__max_large_spot_count = 0
            self.__max_motorbike_spot_count = 0
            self.__max_electric_spot_count = 0

            self.__entrance_panels = {}
            self.__exit_panels = {}
            self.__parking_floors = {}

            # all active parking tickets, identified by their ticket number
            self.__active_tickets = {}

            self.__lock = threading.Lock()

    def __init__(self, name, address):
        if not ParkingLot.instance:
            ParkingLot.instance = ParkingLot.__OnlyOne(name, address)
        else:
            ParkingLot.instance.__name = name
            ParkingLot.instance.__address = address

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def get_new_parking_ticket(self, vehicle):
        if self.is_full(vehicle.get_type()):
            raise Exception("Parking is Full!")
        # synchronizing to allow multiple entrances panels to issue a new
        # parking ticket without interfering with each other
        self.__lock.acquire()
        ticket = ParkingTicket()
        vehicle.assign_ticket(ticket)
        ticket.save_in_DB()
        # if ticket is successfully saved in DB, we can increment parking spot count
        self.__increment_spot_count(vehicle.get_type())
        self.__active_tickets.put(ticket.get_ticket_number(), ticket)
        self.__lock.release()
        return ticket

    def is_full(self, type):
        # trucks and vans can only be parked in LargeSpot
        if type == VehicleType.TRUCK or type == VehicleType.VAN:
            return self.__large_spot_count >= self.__max_large_count

        # motorbikes can only be parked at motorbike spots
        if type == VehicleType.MOTORBIKE:
            return self.__motorbike_spot_count >= self.__max_motorbike_count

        # cars can be parked at compact or large spots
        if type == VehicleType.CAR:
            return (self.__compact_spot_count + self.__large_spot_count) >= (
                    self.__max_compact_count + self.__max_large_count)

        # electric car can be parked at compact, large or electric spots
        return (self.__compact_spot_count + self.__large_spot_count + self.__electric_spot_count) >= (
                self.__max_compact_count + self.__max_large_count
                + self.__max_electric_count)

    def increment_spot_count(self, type):
        large_spot_count = 0
        motorbike_spot_count = 0
        compact_spot_count = 0
        electric_spot_count = 0
        if type == VehicleType.TRUCK or type == VehicleType.VAN:
            large_spot_count += 1
        elif type == VehicleType.MOTORBIKE:
            motorbike_spot_count += 1
        elif type == VehicleType.CAR:
            if self.__compact_spot_count < self.__max_compact_count:
                compact_spot_count += 1
            else:
                large_spot_count += 1
        else:  # electric car
            if self.__electric_spot_count < self.__max_electric_count:
                electric_spot_count += 1
            elif self.__compact_spot_count < self.__max_compact_count:
                compact_spot_count += 1
            else:
                large_spot_count += 1

        def is_full(self):
            for key in self.__parking_floors:
                if not self.__parking_floors.get(key).is_full():
                    return False
            return True

        def add_parking_floor(self, floor):
            # store in database
            None

        def add_entrance_panel(self, entrance_panel):
            # store in database
            None

        def add_exit_panel(self, exit_panel):
            # store in database
            None


class ParkingTicket:
    pass

class ParkingRate:
    pass
