from typing import List
from .enumerations import BookingStatus
from .payment import Payment
from .seat import Seat
from .movie import MovieTicket

class Booking:

    def __init__(self, booking_id, amount, total_seats, created_on, status, payment):
        self.__booking_id = booking_id
        self.__amount = amount
        self.__total_seats = total_seats
        self.__created_on = created_on
        self.__status: BookingStatus = status

        # class instances
        self.__payment: Payment = payment
        self.__tickets: List[MovieTicket] = []
        self.__seats: List[Seat] = []
