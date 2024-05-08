from enum import Enum


class PieceType:
    ROOK = "rook"
    KNIGHT = "knight"
    BISHOP = "bishop"
    QUEEN = "queen"
    KING = "king"
    PAWN = "pawn"


CHESS_BOARD_SIZE = 8

INITIAL_PIECE_SET_SINGLE = [
    (PieceType.ROOK, 0, 0),
    (PieceType.KNIGHT, 1, 0),
    (PieceType.BISHOP, 2, 0),
    (PieceType.QUEEN, 3, 0),
    (PieceType.KING, 4, 0),
    (PieceType.BISHOP, 5, 0),
    (PieceType.KNIGHT, 6, 0),
    (PieceType.ROOK, 7, 0),
    (PieceType.PAWN, 0, 1),
    (PieceType.PAWN, 1, 1),
    (PieceType.PAWN, 2, 1),
    (PieceType.PAWN, 3, 1),
    (PieceType.PAWN, 4, 1),
    (PieceType.PAWN, 5, 1),
    (PieceType.PAWN, 6, 1),
    (PieceType.PAWN, 7, 1)
]

class GameStatus(Enum):

    ACTIVE = 1
    BLACK_WIN = 2
    WHITE_WIN = 3
    FOREFEIT = 4
    STALEMATE = 5
    RESIGNATION = 6


class AccountStatus(Enum):

    ACTIVE = 1
    CLOSED = 2
    CANCELED = 3
    BLACKLISTED = 4
    NONE = 5


class Person:

    def __init__(self, name, street_address, city, state, zipcode, country):
        self.__name = name
        self.__street_address = street_address
        self.__city = city
        self.__state = state
        self.__zip_code = zipcode
        self.__country = country