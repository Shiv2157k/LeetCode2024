from typing import List, Tuple
from collections import deque


class SurroundedRegions:


    def solve_v0(self, board: List[List[str]]) -> None:
        """
        Approach: DFS
        T: O()
        S: O()
        :param board:
        :return:
        """
        # validation
        if not board or not board[0]:
            return

        rows: int = len(board)
        cols: int = len(board[0])
        borders = []

        # Step 1: construct list of border cells
        for row in range(rows):
            borders.append((row, 0))
            borders.append((row, cols - 1))

        for col in range(cols):
            borders.append((0, col))
            borders.append((rows - 1, col))

        # Step 2: Perform DFS or BFS to mark the borders
        # to avoid capture
        for row, col in borders:
            # dfs
            # bfs
            pass

        # Step 3: Capture 0's and unmark borders
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "0":
                    board[row][col] = "X"
                elif board[row][col] == "S":
                    board[row][col] = "0"

    def _depth_first_search(self, row: int, col: int, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        if row < 0 or row > rows - 1 or col < 0 or col > cols - 1:
            return

        if board[row][col] != "0":
            return

        board[row][col] = "S"

        for direction in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            dr = row + direction[0]
            dc = col + direction[1]
            self._depth_first_search(dr, dc, board)

    def _breath_first_search(self, row: int, col: int, board: List[List[str]]) -> None:
        """
        Approach: BFS
        T: O()
        S: O()
        :param board:
        :return:
        """

        queue = deque([(row, col)])

        while queue:
            row, col = queue.popleft()

            if board[row][col] != "0":
                continue

            board[row][col] = "S"
            for direction in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                dr = direction[0]
                dc = direction[1]
                if 0 <= dr < len(board) and 0 <= dc < len(board[0]):
                    queue.append((dr, dc))


