from typing import List


class TicTacToeV1:

    def __init__(self, n: int):
        self.__n = n
        self.__rows = [0] * n
        self.__cols = [0] * n
        self.__diagonal = 0
        self.__anti_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:

        curr_player = 1 if player == 1 else -1

        self.__rows[row] += curr_player
        self.__cols[col] += curr_player

        if row == col:
            self.__diagonal += curr_player

        if col == self.__n - row - 1:
            self.__anti_diagonal += curr_player
            
        if abs(self.__rows[row]) == self.__n or abs(self.__cols[col]) == self.__n or abs(
                self.__diagonal) == self.__n or abs(self.__anti_diagonal) == self.__n:
            return player
        return 0


class TicTacToeV0:

    def __init__(self, n: int):
        self.__board: List[List[int]] = [[0] * n for _ in range(n)]
        self.__n = n

    def move(self, row: int, col: int, player: int):

        self.__board[row][col] = player

        if self.__check_row(row, player) or self.__check_col(row, player) or self.__check_diagonal(
                player) or self.__check_anti_diagonal(player):
            return player
        return 0

    def __check_row(self, row: int, player: int) -> bool:

        for col in range(self.__n):
            if self.__board[row][col] != player:
                return False
        return True

    def __check_col(self, col: int, player: int) -> bool:

        for row in range(self.__n):
            if self.__board[row][col] != player:
                return False
        return True

    def __check_diagonal(self, player: int) -> bool:

        for row in range(self.__n):
            if self.__board[row][row] != player:
                return False
        return True

    def __check_anti_diagonal(self, player: int) -> bool:

        for row in range(self.__n):
            if self.__board[row][self.__n - row - 1] != player:
                return False
        return True
