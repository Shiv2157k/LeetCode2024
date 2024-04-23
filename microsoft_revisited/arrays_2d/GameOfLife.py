from typing import List, Tuple


class GameOfLife:

    def game_of_life(self, board: List[List[int]]) -> None:
        """
        Approach: In place
        T: O(M * N)
        S: O(1)
        :param board:
        :return:
        """
        rows: int = len(board)
        cols: int = len(board[0])

        neighbors: List[Tuple] = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for row in range(rows):
            for col in range(cols):

                live_neighbors: int = 0

                for neighbor in neighbors:
                    dr = row + neighbor[0]
                    dc = col + neighbor[1]

                    if 0 <= dr < rows and 0 <= dc < cols and abs(board[dr][dc]) == 1:
                        live_neighbors += 1

                # Rule 1 or 3
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = -1
                # Rule 4
                if board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 2

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == -1:
                    board[row][col] = 0
                if board[row][col] == 2:
                    board[row][col] = 1
