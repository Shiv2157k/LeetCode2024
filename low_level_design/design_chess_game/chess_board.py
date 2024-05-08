from .pieces import Piece
from typing import List


class Box:

    def __init__(self, piece: Piece, row: int, col: int):
        self.__piece = Piece
        self.__row = row
        self.__col = col


class ChessBoard:

    def __init__(self, boxes: List[Box], creation_date):
        self.__boxes = boxes
        self.__creation_date = creation_date

    def get_pieces(self):
        pass

    def reset_board(self):
        pass

    def update_board(self):
        pass