from abc import ABC
from datetime import datetime
from .constants import BookingStatus


class RoomBooking:

    def __init__(self, booking_id: int, start_date: int, duration_in_days: int, booking_status: BookingStatus):
        self.__booking_id = booking_id
        self.__start_date = start_date
        self.__duration_in_days = duration_in_days
        self.__status = booking_status
        self.__check_in = None
        self.__check_out = None

        self.__guest_id = 0
        self.__room = None
        self.__invoice = None
        self.__notifications = []

    def fetch_details(self, booking_id: int):
        pass


class Invoice:

    def __init__(self):
        self.__amount: float = 0.0
        self.__invoice_item = []

    def create_bill(self, invoice_item):
        self.__invoice_item.append(invoice_item)


class InvoiceItem:

    def __init__(self, amount: float):
        self.__amount = amount

    def update_amount(self, amount: float):
        self.__amount += amount


class RoomCharge(ABC):

    def __init__(self):
        self.__issue_at = datetime.today()

    def add_invoice_item(self, invoice_item: InvoiceItem):
        pass


class Amenity(RoomCharge):

    def __init__(self, name: str, description: str):
        super().__init__()
        self.__name = name
        self.__description = description


class KitchenService(RoomCharge):

    def __init__(self, description: str):
        super().__init__()
        self.__description = description


class RoomService(RoomCharge):

    def __init__(self, is_chargeable: bool, request_item: str):
        super().__init__()
        self.__is_chargeable = is_chargeable
        self.__request_item = request_item
