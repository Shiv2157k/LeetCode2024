from collections import defaultdict
from pprint import pprint
from typing import List


class SudokuSolver:

    def solve(self, board: List[List[str]]) -> (List[List[str]], bool):
        """
        Approach: BackTracking
        :param board:
        :return:
        """

        # couldPlace the number
        def couldPlace(num: int, row: int, col: int):
            return not (num in rows[row] or num in cols[col] or num in boxes[boxIndex(row, col)])

        # place number
        def placeNumber(num: int, row: int, col: int):
            rows[row][num] += 1
            cols[col][num] += 1
            boxes[boxIndex(row, col)][num] += 1
            board[row][col] = str(num)

        # place next number
        def placeNextNumber(row: int, col: int):
            if row == N - 1 and col == N - 1:
                nonlocal sudokuSolved
                sudokuSolved = True
            else:
                if col == N - 1:
                    backtrack(row + 1, 0)
                else:
                    backtrack(row, col + 1)

        # remove the number
        def removeNumber(num: int, row: int, col: int):
            del rows[row][num]
            del cols[col][num]
            del boxes[boxIndex(row, col)][num]
            board[row][col] = "."

        # backtrack
        def backtrack(row: int=0, col: int=0):
            if board[row][col] == ".":
                for num in range(1, 10):
                    if couldPlace(num, row, col):
                        placeNumber(num, row, col)
                        placeNextNumber(row, col)

                        if not sudokuSolved:
                            removeNumber(num, row, col)
            else:
                placeNextNumber(row, col)

        # initiate rows, cols and boxes for above steps
        n = 3
        N = n * n

        # to calculate boxIndex
        boxIndex = lambda row, col: (row // n) * n + col // n

        rows = [defaultdict(int) for _ in range(N)]
        cols = [defaultdict(int) for _ in range(N)]
        boxes = [defaultdict(int) for _ in range(N)]

        for row in range(N):
            for col in range(N):
                if board[row][col].isnumeric():
                    digit = int(board[row][col])
                    placeNumber(digit, row, col)

        sudokuSolved = False
        backtrack()
        return (board, sudokuSolved)


if __name__ == "__main__":

    sudoku = SudokuSolver()
    pprint(sudoku.solve(
        [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    ))
