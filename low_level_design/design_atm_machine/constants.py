from enum import Enum, auto

class ATMState(Enum):

    IDLE = auto
    HAS_CARD = auto
    SELECT_OPTION = auto
    WITHDRAW = auto
    TRANSFER_MONEY = auto
    BALANCE_INQUIRY = auto


class User:

    def __init__(self, card, account):
        self.__card = card
        self.__account = account


class ATMCard:

    def __init__(self, card_number, customer_name, card_expiry_date, pin):
        self.__card_number = card_number
        self.__customer_name = customer_name
        self.__card_expiry_date = card_expiry_date
        self.__pin = pin