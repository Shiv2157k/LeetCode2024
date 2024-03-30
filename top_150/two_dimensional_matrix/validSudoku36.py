from typing import List


class Sudoku:

    def isValidBoardV2(self, board: List[List[str]]) -> bool:
        """
        Approach: Bit Mask and Bit Manipulation
        T: O(N^2)
        S: O(N)
        :param board:
        :return:
        """
        N = 9
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        # To Check if it already exists
        # row/col/boxIndex & (row/col/boxIndex << pos)

        # To add
        # row/col/ boxIndex | (row/col/boxIndex << pos)

        for row in range(N):
            for col in range(N):

                if board[row][col].isnumeric():

                    pos = int(board[row][col]) - 1

                    if rows[row] & (1 << pos):
                        return False
                    rows[row] = rows[row] | (1 << pos)

                    if cols[col] & (1 << pos):
                        return False
                    cols[col] = cols[col] | (1 << pos)

                    boxIndex = (row // 3) * 3 + (col // 3)
                    if boxes[boxIndex] & (1 << pos):
                        return False
                    boxes[boxIndex] = boxes[boxIndex] | (1 << pos)
        return True

    def isValidBoardV1(self, board: List[List[str]]) -> bool:
        """
        Approach: Fixed Length List
        T: O(N^2)
        S: O(N^2)
        :param board:
        :return:
        """

        N = 9

        rows = [[0] * N for _ in range(N)]
        cols = [[0] * N for _ in range(N)]
        boxes = [[0] * N for _ in range(N)]

        for row in range(N):
            for col in range(N):

                if board[row][col].isnumeric():

                    pos = int(board[row][col]) - 1

                    if rows[row][pos] == 1:
                        return False
                    rows[row][pos] = 1

                    if cols[col][pos] == 1:
                        return False
                    cols[col][pos] = 1

                    boxIdx = (row // 3) * 3 + (col // 3)
                    if boxes[boxIdx][pos] == 1:
                        return False
                    boxes[boxIdx][pos] = 1
        return True

    def isValidBoardV0(self, board: List[List[str]]) -> bool:
        """
        Approach: Hash Set
        T: O(N^2)
        S: O(N^2)
        :param board:
        :return:
        """
        N = 9

        # initialize rows, cols, boxes set
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for row in range(N):
            for col in range(N):

                if board[row][col].isnumeric():

                    val = board[row][col]

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


if __name__ == "__main__":
    sudoku = Sudoku()
    print(sudoku.isValidBoardV0(
        [["5", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    ))
    print(sudoku.isValidBoardV0(
        [["8", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    ))

    print(sudoku.isValidBoardV1(
        [["5", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    ))
    print(sudoku.isValidBoardV1(
        [["8", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    ))

    print(sudoku.isValidBoardV2(
        [["5", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    ))
    print(sudoku.isValidBoardV2(
        [["8", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    ))
