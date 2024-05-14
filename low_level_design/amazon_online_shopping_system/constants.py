from enum import Enum


class Address:

    def __init__(self, zip_code, address, city, state, country):
        self.__zip_code = zip_code
        self.__address = address
        self.__city = city
        self.__state = state
        self.__country = country


class OrderStatus(Enum):
    UNSHIPPED = 1
    PENDING = 2
    SHIPPED = 3
    CONFIRMED = 4
    CANCELED = 5
    REFUNDED = 6


class AccountStatus(Enum):
    ACTIVE = 1
    INACTIVE = 2
    BLOCKED = 3


class ShipmentStatus(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3
    ON_HOLD = 4


class PaymentStatus(Enum):
    CONFIRMED = 1
    DECLINED = 2
    PENDING = 3
    REFUNDED = 4