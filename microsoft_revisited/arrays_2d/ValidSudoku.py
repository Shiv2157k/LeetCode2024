from typing import List


class Sudoku:

    def isValidV2(self, board: List[List[str]]) -> bool:
        """
        Approach: Bit Manipulation
        T: O(1)
        S: O(N
        :param board:
        :return:
        """
        N = 9
        rows = [0] * N
        cols = [0] * N
        boxes = [0] * N

        for row in range(N):
            for col in range(N):

                val = board[row][col]

                if val == '.':
                    continue

                ptr = ord(val) - ord('1')

                if rows[row] & (1 << ptr):
                    return False
                rows[row] = rows[row] | (1 << ptr)

                if cols[col] & (1 << ptr):
                    return False
                cols[col] = cols[col] | (1 << ptr)

                boxIdx = (row // 3) * 3 + (col // 3)
                if boxes[boxIdx] & (1 << ptr):
                    return False
                boxes[boxIdx] = boxes[boxIdx] | (1 << ptr)
        return True

    def isValidV1(self, board: List[List[str]]) -> bool:
        """
        Approach: List
        T: O(N * N)
        S: O(N * N)
        :param board:
        :return:
        """

        N = 9

        rows = [[0] * N for _ in range(N)]
        cols = [[0] * N for _ in range(N)]
        boxes = [[0] * N for _ in range(N)]

        for row in range(N):
            for col in range(N):

                val = board[row][col]

                if val == '.':
                    continue

                ptr = ord(val) - ord('1')

                if rows[row][ptr] == 1:
                    return False
                rows[row][ptr] = 1

                if cols[col][ptr] == 1:
                    return False
                cols[col][ptr] = 1

                boxIdx = (row // 3) * 3 + (col // 3)
                if boxes[boxIdx][ptr] == 1:
                    return False
                boxes[boxIdx][ptr] = 1
        return True

    def isValidV0(self, board: List[List[str]]) -> bool:
        """
        Approach: Hash Set
        T: O(N * N)
        S: O(N * N)
        :param board:
        :return:
        """
        N = 9

        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for row in range(N):
            for col in range(N):

                val = board[row][col]

                if val == '.':
                    continue

                if val in rows[row]:
                    return False
                rows[row].add(val)

                if val in cols[col]:
                    return False
                cols[col].add(val)

                boxIdx = (row // 3) * 3 + (col // 3)
                if val in boxes[boxIdx]:
                    return False
                boxes[boxIdx].add(val)
        return True
