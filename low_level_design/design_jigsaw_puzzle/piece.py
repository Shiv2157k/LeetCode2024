from .side import Side
from typing import List


class Piece:

    def __init__(self):
        self.__sides: List[Side] = [None] * 4

    def check_corner(self):
        pass

    def check_edge(self):
        pass

    def check_middle(self):
        pass
