from typing import List


class GameOfLife:

    def getNextGenerationV0(self, board: List[List[int]]) -> List[List[int]]:
        """
        Approach: Copy Board
        T: O(MN)
        S: O(MN)
        :param board:
        :return:
        """

        rows, cols = len(board), len(board[0])
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

        # Step 1: Copy to new board
        newBoard = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 1:
                    newBoard[row][col] = 1

        for row in range(rows):
            for col in range(cols):

                liveNeighbors = 0

                # calculate the live neighbors
                for neighbor in neighbors:
                    dr = row + neighbor[0]
                    dc = col + neighbor[1]

                    if (0 <= dr < rows) and (0 <= dc < cols) and newBoard[row][col] == 1:
                        liveNeighbors += 1

                # Rule 1 or 3
                if newBoard[row][col] == 1 and (liveNeighbors < 2 or liveNeighbors > 3):
                    board[row][col] = 0
                # Rule 4
                if newBoard[row][col] == 0 and liveNeighbors == 3:
                    board[row][col] = 1
        return board

    def getNextGenerationV1(self, board: List[List[int]]) -> List[List[int]]:
        """
        Approach: In place Board
        T: O(MN)
        S: O(1)
        :param board:
        :return:
        """
        rows, cols = len(board), len(board[0])

        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for row in range(rows):
            for col in range(cols):

                liveNeighbors = 0

                for neighbor in neighbors:
                    dr = row + neighbor[0]
                    dc = col + neighbor[1]

                    if (0 <= dr < rows) and (0 <= dc < cols) and abs(board[row][col]) == 1:
                        liveNeighbors += 1

                # Rule 1 or 3
                if board[row][col] == 1 and (liveNeighbors < 2 or liveNeighbors > 3):
                    board[row][col] = -1
                if board[row][col] == 0 and liveNeighbors == 3:
                    board[row][col] = 2

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == -1:
                    board[row][col] = 0
                elif board[row][col] == 2:
                    board[row][col] = 1
        return board
