from .constants import Suit


class Card:

    def __init__(self, suit: Suit, face_value: int):
        self.__suit = suit
        self.__face_value = face_value

    def get_suit(self):
        return self.__suit

    def get_face_value(self):
        return self.__face_value