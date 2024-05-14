from abc import ABC, abstractmethod


class ATMState(ABC):

    @abstractmethod
    def insert_card(self, atm, card):
        pass

    @abstractmethod
    def authenticate_pin(self, atm, card, pin):
        pass

    @abstractmethod
    def select_operation(self, atm, card, transaction_type):
        pass

    @abstractmethod
    def cash_withdrawal(self, atm, card, withdraw_amount):
        pass

    @abstractmethod
    def display_balance(self, atm, card):
        pass

    @abstractmethod
    def transfer_money(self, atm, card, account_number, transfer_amount):
        pass

    @abstractmethod
    def return_card(self):
        pass

    @abstractmethod
    def exit(self, atm):
        pass


class IdleState(ATMState):

    def insert_card(self, atm, card):
        pass

    def authenticate_pin(self, atm, card, pin):
        pass

    def select_operation(self, atm, card, transaction_type):
        pass

    def cash_withdrawal(self, atm, card, withdraw_amount):
        pass

    def display_balance(self, atm, card):
        pass

    def transfer_money(self, atm, card, account_number, transfer_amount):
        pass

    def return_card(self):
        pass

    def exit(self, atm):
        pass


class HasCardState(ATMState):
    def insert_card(self, atm, card):
        pass

    def authenticate_pin(self, atm, card, pin):
        pass

    def select_operation(self, atm, card, transaction_type):
        pass

    def cash_withdrawal(self, atm, card, withdraw_amount):
        pass

    def display_balance(self, atm, card):
        pass

    def transfer_money(self, atm, card, account_number, transfer_amount):
        pass

    def return_card(self):
        pass

    def exit(self, atm):
        pass


class SelectOperationState(ATMState):

    def insert_card(self, atm, card):
        pass

    def authenticate_pin(self, atm, card, pin):
        pass

    def select_operation(self, atm, card, transaction_type):
        pass

    def cash_withdrawal(self, atm, card, withdraw_amount):
        pass

    def display_balance(self, atm, card):
        pass

    def transfer_money(self, atm, card, account_number, transfer_amount):
        pass

    def return_card(self):
        pass

    def exit(self, atm):
        pass


class CheckBalanceState(ATMState):

    def insert_card(self, atm, card):
        pass

    def authenticate_pin(self, atm, card, pin):
        pass

    def select_operation(self, atm, card, transaction_type):
        pass

    def cash_withdrawal(self, atm, card, withdraw_amount):
        pass

    def display_balance(self, atm, card):
        pass

    def transfer_money(self, atm, card, account_number, transfer_amount):
        pass

    def return_card(self):
        pass

    def exit(self, atm):
        pass


class CashWithdrawalState(ATMState):

    def insert_card(self, atm, card):
        pass

    def authenticate_pin(self, atm, card, pin):
        pass

    def select_operation(self, atm, card, transaction_type):
        pass

    def cash_withdrawal(self, atm, card, withdraw_amount):
        pass

    def display_balance(self, atm, card):
        pass

    def transfer_money(self, atm, card, account_number, transfer_amount):
        pass

    def return_card(self):
        pass

    def exit(self, atm):
        pass


class TransferMoneyState(ATMState):

    def insert_card(self, atm, card):
        pass

    def authenticate_pin(self, atm, card, pin):
        pass

    def select_operation(self, atm, card, transaction_type):
        pass

    def cash_withdrawal(self, atm, card, withdraw_amount):
        pass

    def display_balance(self, atm, card):
        pass

    def transfer_money(self, atm, card, account_number, transfer_amount):
        pass

    def return_card(self):
        pass

    def exit(self, atm):
        pass
