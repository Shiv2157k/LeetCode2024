from enum import Enum


class PaymentStatus(Enum):
    PENDING = 1
    CONFIRMED = 2
    DECLINED = 3
    REFUNDED = 4


class BookingStatus(Enum):
    PENDING = 1
    CONFIRMED = 2
    CANCELLED = 3
    DENIED = 4
    REFUNDED = 5


class SeatStatus(Enum):
    AVAILABLE = 1
    BOOKED = 2
    RESERVED = 3
