

class City:

    def __init__(self, name, state, zipcode):
        self.__name = name
        self.__state = state
        self.__zipcode = zipcode


class Cinema:

    def __init__(self, cinema_id, city):
        self.__cinema_id = cinema_id
        self.__city = city
        self.__halls = []


class Hall:

    def __init__(self, hall_id):
        self.__hall_id = hall_id
        self.__shows = []

    def find_current_shows(self):
        pass