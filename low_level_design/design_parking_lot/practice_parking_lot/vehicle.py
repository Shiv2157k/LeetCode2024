from abc import ABC
from constants import VehicleType


class Vehicle(ABC):

    def __init__(self, license_number: str, vehicle_type: VehicleType, ticket: str = None):
        self.__license_number = license_number
        self.__vehicle_type = vehicle_type
        self.__ticket = ticket

    def assign_ticket(self, ticket):
        self.__ticket = ticket

    def get_type(self):
        return self.__vehicle_type


class Car(Vehicle):

    def __init__(self, license_number: str, vehicle_type: VehicleType, ticket: str = None):
        super().__init__(license_number, vehicle_type, ticket)


class Truck(Vehicle):

    def __init__(self, license_number: str, vehicle_type: VehicleType, ticket: str = None):
        super().__init__(license_number, vehicle_type, ticket)


class Van(Vehicle):

    def __init__(self, license_number: str, vehicle_type: VehicleType, ticket: str = None):
        super().__init__(license_number, vehicle_type, ticket)


class Electric(Vehicle):

    def __init__(self, license_number: str, vehicle_type: VehicleType, ticket: str = None):
        super().__init__(license_number, vehicle_type, ticket)
