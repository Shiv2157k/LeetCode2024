from typing import List


class ValidSudoku:

    def is_valid_v1(self, board: List[List[str]]) -> bool:
        """
        Approach: Bit Manipulation
        t: O(MN)
        s: O(N)
        :param board:
        :return:
        """

        N = 9
        rows = [0] * N
        cols = [0] * N
        boxes = [0] * N

        for row in range(N):
            for col in range(N):

                if board[row][col].isdigit():

                    pos = ord(board[row][col]) - ord('1')

                    if rows[pos] & (1 << pos):
                        return False
                    rows[pos] |= (1 << pos)

                    if cols[pos] & (1 << pos):
                        return False
                    cols[col] |= (1 << pos)

                    box_idx = (row // 3) * 3 + (col // 3)
                    if boxes[box_idx] & (1 << pos):
                        return False
                    boxes[box_idx] |= (1 << pos)
        return True

    def is_valid_v1(self, board: List[List[str]]) -> bool:
        """
        Approach: 2D Array
        T: O(N*N)
        S: O(N*N)
        :param board:
        :return:
        """

        N = 9
        rows = [[0] * N for _ in range(N)]
        cols = [[0] * N for _ in range(N)]
        boxes = [[0] * N for _ in range(N)]

        for row in range(N):
            for col in range(N):

                if board[row][col].isdigit():

                    pos = ord(board[row][col]) - ord('1')

                    if rows[row][pos] == 1:
                        return False
                    rows[row][pos] = 1

                    if cols[col][pos] == 1:
                        return False
                    cols[col][pos] = 1

                    box_idx = (row // 3) * 3 + (col // 3)
                    if boxes[box_idx][pos] == 1:
                        return False
                    boxes[box_idx][pos] = 1
        return True

    def is_valid_v0(self, board: List[List[str]]) -> bool:
        """
        Approach: Using Set
        T: O(NM)
        S: O(NM)
        :param board:
        :return:
        """
        N = 9
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for row in range(N):
            for col in range(N):

                if board[row][col].isdigit():

                    val = ord(board[row][col]) - ord('1')

                    if val in rows[row]:
                        return False
                    rows[row].add(val)

                    if val in cols[col]:
                        return False
                    cols[col].add(val)

                    box_idx = (row // 3) * 3 + (col // 3)
                    if val in boxes[box_idx]:
                        return False
                    boxes[box_idx].add(val)
        return True
