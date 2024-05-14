from .card import Card
from .constants import Suit
from datetime import datetime


class Deck:

    def __init__(self, cards):
        self.__cards = []
        """
        self.__creation_date = datetime.today()
        for value in range(1, 14):
            for suit in Suit:
                self.__cards.add()
        """

    def get_cards(self):
        pass


class Shoe:

    def __init__(self, decks, number_of_decks):
        self.__decks = {}
        self.__number_of_decks = number_of_decks

    def create_shoe(self):
        None

    def shuffle(self):
        None

    def deal_card(self):
        None
