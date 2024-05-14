

class __Puzzle(object):

    __instances = None

    def __new__(cls, __Puzzle=None):
        if cls.__instances is None:
            cls.__instances = super(__Puzzle, cls).__new__(cls)
        return cls.__instances


class Puzzle(metaclass=__Puzzle):

    def __init__(self):
        self.__board = [[]]
        self.__free = []

    def insert_piece(self, piece, row, col):
        pass


class PuzzleSolver:

    def match_pieces(self, board):
        pass