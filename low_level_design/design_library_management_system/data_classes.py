class Address:

    def __init__(self, street, city, state, zipcode, country):
        self.__street_address = street
        self.__city = city
        self.__state = state
        self.__zip_code = zipcode
        self.__country = country


class Person:

    def __init__(self, name: str, address: Address, email: str, phone: str):
        self.__name = name
        self.__address = Address
        self.__email = email
        self.__phone = phone
