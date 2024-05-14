

class Account:

    def __init__(self, username, password, name, shipping_address, status, email, phone, credit_cards, bank_accounts):
        self.__user_name = username
        self.__password = password
        self.__name = name
        self.__shipping_address = shipping_address
        self.__status = status
        self.__email = email
        self.__phone = phone
        self.__credit_cards = credit_cards
        self.__bank_accounts = bank_accounts


    def get_shipping_address(self):
        pass

    def add_product(self, product):
        pass

    def add_product_review(self, review, product):
        pass

    def delete_product(self, product):
        pass

    def delete_product_review(self, review, product):
        pass

    def reset_password(self):
        pass