from typing import List


class GameOfLife:

    def game_of_life_v1(self, board: List[List[int]]) -> List[int]:
        """
        Approach: in-place
        T: O(N * M)
        S: O(1)
        :param board:
        :return:
        """

        rows = len(board)
        cols = len(board[0])

        directions = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1))

        for row in range(rows):
            for col in range(cols):

                live_neighbors = 0

                for direction in directions:
                    dr = row + direction[0]
                    dc = col + direction[1]

                    if 0 <= dr < rows and 0 <= dc < cols and abs(board[row][col]) == 1:
                        live_neighbors += 1

                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = -1
                if board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 2

        for row in range(rows):
            for col in range(cols):

                if board[row][col] == -1:
                    board[row][col] = 0
                elif board[row][col] == 2:
                    board[row][col] = 1
        return board

    def game_of_life_v0(self, board: List[List[int]]) -> List[int]:
        """
        Approach: Duplicated Board
        T: O(N * M)
        S: O(N * M)
        :param board:
        :return:
        """

        rows = len(board)
        cols = len(board[0])
        new_board = [[0] * cols for _ in range(rows)]
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1))

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 1:
                    new_board[row][col] = 1

        for row in range(rows):
            for col in range(cols):

                live_neighbors = 0

                for direction in directions:
                    dr = row + direction[0]
                    dc = col + direction[1]

                    if 0 <= dr < rows and 0 <= dc < cols and board[dr][dc] == 1:
                        live_neighbors += 1
                if new_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    new_board[row][col] = 0
                if new_board[row][col] == 0 and live_neighbors == 3:
                    new_board[row][col] = 1
        return new_board
