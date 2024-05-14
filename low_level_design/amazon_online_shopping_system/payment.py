from abc import ABC, abstractmethod


class Payment(ABC):

    def __init__(self, amount, timestamp, status):
        self.__amount = amount
        self.__timestamp = timestamp
        self.__status = status

    @abstractmethod
    def make_payment(self):
        pass


class CreditCard(Payment):

    def __init__(self, amount, timestamp, status, name_on_card, card_number, billing_address, code):
        self.__name_on_card = name_on_card
        self.__card_number = card_number
        self.__billing_address = billing_address
        self.__code = code
        super().__init__(amount, timestamp, status)

    def make_payment(self):
        pass


class ElectronicBankTransfer(Payment):

    def __init__(self, amount, timestamp, status, bank_name, routing_number, account_number, billing_address):

        self.__bank_name = bank_name
        self.__account_number = account_number
        self.__routing_number = routing_number
        self.__billing_address = billing_address
        super().__init__(amount, timestamp, status)

        # Returns the PaymentStatus enum
        def make_payment(self):
            # functionality
            pass

class Cash(Payment):
    def __init__(self, amount, timestamp, status, billing_address):
        self.__billing_address = billing_address
        super().__init__(amount, timestamp, status)

    # Returns the PaymentStatus enum
    def make_payment(self):
        # functionality
        pass