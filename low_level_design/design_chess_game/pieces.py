from abc import ABC, abstractmethod

class Piece(ABC):

    def __init__(self, killed, white):
        self.__killed = killed
        self.__white = white

    def is_white(self):
        pass

    def is_killed(self):
        pass

    @abstractmethod
    def can_move(self, board, start, end):
        pass


class King(Piece):

    def __init__(self, killed, white, castling_done):
        super().__init__(killed, white)
        self.__castling_done = castling_done

    def can_move(self, board, start, end):
        pass


class Queen(Piece):

    def __init__(self, killed, white):
        super().__init__(killed, white)

    def can_move(self, board, start, end):
        pass

class Knight(Piece):
    def __init_(self, killed, white):
        super().__init__(killed, white)

    def can_move(self, board, start, end):
        pass


class Bishop(Piece):
    def __init_(self, killed, white):
        super().__init__(killed, white)

    def can_move(self, board, start, end):
        pass


class Rook(Piece):
    def __init_(self, killed, white):
        super().__init__(killed, white)

    def can_move(self, board, start, end):
        pass


class Pawn(Piece):
    def __init_(self, killed, white):
        super().__init__(killed, white)

    def can_move(self, board, start, end):
        pass