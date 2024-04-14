from enum import Enum
from datetime import datetime
from collections import defaultdict


class Card:
    def __init__(self):
        self.cardNumber = ""
        self.customerName = ""
        self.expiryDate = datetime.now()
        self.pin = 0
        self.withdrawLimit = 0.0

class Transaction:
    def __init__(self):
        self.transactionId = 0
        self.transactionDate = datetime.now()
        self.sourceAmount = 0
        self.transactionStatus = TransactionStatus.PENDING
        self.transactionType = TransactionType.BALANCE_ENQUIRY


class CardReader:
    def get_card_details(self):
        return None


class Cash:
    def __init__(self):
        self.cashType = CashType.FIVE
        self.serialNumber = ""


class CashDispenser:
    def __init__(self):
        self.cashAvailable = defaultdict(list)

    def dispense_cash(self, amount):
        pass


class CashType(Enum):
    FIVE = 1
    TWENTY = 2


class KeyPad:
    def get_input(self):
        return None


class Printer:
    def print_message(self):
        return None


class Screen:
    def display(self, message):
        pass


class Account:
    def __init__(self):
        self.accountNumber = 0
        self.accountBalance = 0.0


class Address:
    def __init__(self):
        self.zipCode = 0
        self.street = ""
        self.city = ""
        self.country = ""


class CustomerStatus(Enum):
    ACTIVE = 1
    BLOCKED = 2
    CLOSED = 3


class Customer:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.phone = ""
        self.card = Card()
        self.account = Account()
        self.customerStatus = CustomerStatus.ACTIVE


class BalanceInquiry(Transaction):
    def get_account(self):
        return None


class Deposit(Transaction):
    def __init__(self):
        self.amount = 0.0


class CashDeposit(Deposit):
    def get_cash(self):
        return []


class CheckDeposit:
    def __init__(self):
        self.checkNumber = ""

    def get_check_number(self):
        return None


class TransactionStatus(Enum):
    SUCCESS = 1
    CANCELLED = 2
    PENDING = 3
    ERROR = 4


class TransactionType(Enum):
    BALANCE_ENQUIRY = 1
    DEPOSIT = 2
    WITHDRAW = 3
    TRANSFER = 4


class Transfer(Transaction):
    def __init__(self):
        super().__init__()
        self.destinationAccount = 0
        self.amount = 0.0


class Withdraw(Transaction):
    def __init__(self):
        super().__init__()
        self.amount = 0.0


class ATM:
    def __init__(self):
        self.atmID = 0
        self.location = Address()
        self.cashDispenser = CashDispenser()
        self.screen = Screen()
        self.cardReader = CardReader()
        self.keyPad = KeyPad()
        self.checkDeposit = CheckDeposit()
        self.cashDeposit = CashDeposit()
        self.printer = Printer()

    def authenticate(self, card):
        return False

    def execute_transaction(self, customer, transaction):
        return False


class Bank:
    def __init__(self):
        self.bankName = ""
        self.location = Address()
        self.atmlList = []
