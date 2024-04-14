class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.antiDiagonal = 0

    def move(self, row: int, col: int, player: int) -> int:

        currentPlayer = 1 if player == 1 else -1

        self.rows[row] += currentPlayer
        self.cols[col] += currentPlayer

        if row == col:
            self.diagonal += currentPlayer

        if col == self.n - row - 1:
            self.antiDiagonal += currentPlayer

        # winner check
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.diagonal) == self.n or abs(
                self.antiDiagonal) == self.n:
            return player

        return 0
