from typing import List


class TicTacToeV1:

    def __init__(self, n: int):
        self._n: int = n
        self._rows: List[int] = [0] * n
        self._cols: List[int] = [0] * n
        self._diagonal: int = 0
        self._anti_diagonal: int = 0

    def move(self, row: int, col: int, player: int) -> int:

        current_player = 1 if player == 1 else -1

        self._rows[row] += current_player
        self._cols[col] += current_player

        if row == col:
            self._diagonal += current_player
        if col == self._n - row - 1:
            self._anti_diagonal += current_player

        # winner check
        if (abs(self._rows[row]) == self._n or
                abs(self._cols[col]) == self._n or
                abs(self._diagonal) == self._n or
                abs(self._anti_diagonal) == self._n):
            return player
        return 0


class TicTacToeV0:

    def __init__(self, n: int):
        self.board: List[List[int]] = [[0] * n for _ in range(n)]
        self.n = n

    def move(self, row: int, col: int, player: int):

        self.board[row][col] = player

        if (self._check_row(row, player)) or (self._check_col(col, player)) or (
                row == col and self._check_diagonal(player)) or (
                col == self.n - row - 1 and self._check_anti_diagonal(player)):
            return player
        return 0

    def _check_row(self, row: int, player: int) -> bool:

        for col in range(self.n):
            if self.board[row][col] != player:
                return False
        return True

    def _check_col(self, col: int, player: int) -> bool:

        for row in range(self.n):
            if self.board[row][col] != player:
                return False
        return True

    def _check_diagonal(self, player: int) -> bool:

        for row in range(self.n):
            if self.board[row][row] != player:
                return False
        return True

    def _check_anti_diagonal(self, player: int) -> bool:
        for row in range(self.n):
            if self.board[row][self.n - row - 1] != player:
                return False
        return True
