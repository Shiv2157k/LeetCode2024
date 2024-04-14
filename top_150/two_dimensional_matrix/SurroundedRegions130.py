from typing import List
from collections import deque


class SurroundedRegions:

    def __init__(self):
        self.rows = 0
        self.cols = 0

    def captureV0(self, board: List[List[int]]) -> List[List[int]]:
        """
        Approach: DFS
        T: O(N)
        S: O(N)
        :param board:
        :return:
        """

        if not board or not board[0]:
            return []

        self.rows, self.cols = len(board), len(board[0])

        # Step 1: capture the four side border row, col
        borders = []

        for row in range(self.rows):
            borders.append((row, 0))
            borders.append((row, self.cols - 1))

        for col in range(self.cols):
            borders.append((0, col))
            borders.append((self.rows - 1, col))

        # Step 2: Traverse through border and mark them
        for row, col in borders:
            # self.depthFirstSearch(board, row, col)
            self.breadthFirstSearch(board, row, col)

        # Step 3: Mark and Flip
        for row in range(self.rows):
            for col in range(self.cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "$":
                    board[row][col] = "O"

    def depthFirstSearch(self, board: List[List[int]], row: int, col: int):
        """
        :param board:
        :return:
        """

        if board[row][col] != "O":
            return

        board[row][col] = "$"

        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dr = row + direction[0]
            dc = col + direction[1]
            if 0 <= dr < self.rows and 0 <= dc < self.cols:
                self.depthFirstSearch(board, dr, dc)

    def breadthFirstSearch(self, board: List[List[int]], row: int, col: int):

        queue = deque([(row, col)])

        while queue:

            row, col = queue.popleft()

            if board[row][col] != "O":
                continue
            board[row][col] = "$"

            for direction in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                dr = row + direction[0]
                dc = col + direction[1]
                if 0 <= dr < self.rows and 0 <= dc < self.cols:
                    queue.append((dr, dc))
