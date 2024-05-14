from abc import ABC, abstractmethod


class State(ABC):

    def insert_money(self, machine, amount):
        pass

    def press_button(self, machine, rack_number):
        pass

    def return_change(self, amount):
        pass

    def update_inventory(self, machine, rack_number):
        pass

    def dispense_product(self, machine, rack_number):
        pass


class NoMoneyInsertedState(State):

    def __init__(self):
        pass

    def insert_money(self, machine, amount):
        pass

    def press_button(self, machine, rack_number):
        pass

    def return_change(self, amount):
        pass

    def update_inventory(self, machine, rack_number):
        pass

    def dispense_product(self, machine, rack_number):
        pass


class MoneyInsertedState(State):

    def __init__(self):
        pass

    def insert_money(self, machine, amount):
        pass

    def press_button(self, machine, rack_number):
        # check if product item is available
        # validate money
        # change state to DispenseState
        pass

    def return_change(self, amount):
        pass

    def update_inventory(self, machine, rack_number):
        pass

    def dispense_product(self, machine, rack_number):
        pass


class DispenseState(State):

    def __init__(self):
        pass

    def insert_money(self, machine, amount):
        pass

    def press_button(self, machine, rack_number):
        pass

    def return_change(self, amount):
        pass

    def update_inventory(self, machine, rack_number):
        pass

    def dispense_product(self, machine, rack_number):
        # dispense product
        # change state to NoMoneyInsertedState
        pass