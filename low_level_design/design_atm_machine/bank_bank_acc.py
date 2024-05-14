from abc import ABC, abstractmethod


class Bank:

    def __init__(self, name, bank_code, available_balance):
        self.__name = name
        self.__bank_code = bank_code
        self.__available_balance = available_balance

    def get_bank_code(self):
        pass

    def add_ATM(self):
        pass


class BankAccount:

    def __init__(self, account_number, total_balance, available_balance):
        self.__account_number = account_number
        self.__total_balance = total_balance
        self.__available_balance = available_balance

    def get_available_balance(self):
        pass


class SavingsAccount(BankAccount):

    def __init__(self, account_number, total_balance, available_balance):
        super().__init__(account_number, total_balance, available_balance)

    def get_withdraw_limit(self):
        pass


class CheckingAccount(BankAccount):

    def __init__(self, account_number, total_balance, available_balance):
        super().__init__(account_number, total_balance, available_balance)

    def get_withdraw_limit(self):
        pass
