class ATM:

    def __init__(self, current_atm_state, atm_balance, hundred_dollar_bills, fifty_dollar_bills, ten_dollar_bills):
        self.__current_atm_state = current_atm_state
        self.__atm_balance = atm_balance
        self.__hundred_dollar_bills = hundred_dollar_bills
        self.__fifty_dollar_bills = fifty_dollar_bills
        self.__ten_dollar_bills = ten_dollar_bills

    def display_current_state(self):
        pass

    def initialise_atm(self, atm_balance, hundred_dollar_bills, fifty_dollar_bills, ten_dollar_bills):
        pass


class ATMRoom:

    def __init__(self, atm, user):
        self.__atm = atm
        self.user = user
