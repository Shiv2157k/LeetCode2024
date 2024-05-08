from .pieces import Piece


class Move:

    def __init__(self, start: int, end: int, piece_killed: Piece, piece_moved: Piece, player: Player, castling_move: bool):
        self.__start = start
        self.__end = end
        self.__piece_killed = piece_killed
        self.__piece_moved = piece_moved
        self.__player = player
        self.__castling_move = castling_move


    def is_castling_move(self):
        return self.is_castling_move()