from abc import ABC, abstractmethod


class Seat(ABC):

    def __init__(self, seat_no, status):
        self.__seat_no = seat_no
        self.__status = status

    def is_available(self):
        pass

    @abstractmethod
    def set_seat(self):
        pass

    @abstractmethod
    def set_rate(self):
        pass


class Platinum(Seat):

    def __init__(self, seat_no, status, rate):
        self.__rate = rate
        super().__init__(seat_no, status)

    def set_rate(self):
        pass

    def set_seat(self):
        pass


class Gold(Seat):

    def __init__(self, seat_no, status, rate):
        self.__rate = rate
        super().__init__(seat_no, status)

    def set_seat(self):
        pass

    def set_rate(self):
        pass


class Silver(Seat):

    def __init__(self, seat_no, status, rate):
        self.__rate = rate
        super().__init__(seat_no, status)

    def set_seat(self):
        pass

    def set_rate(self):
        pass