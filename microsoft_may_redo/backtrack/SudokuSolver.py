from typing import List
from collections import defaultdict


class SudokuSolver:

    def solved(self, board: List[List[str]]) -> List[List[str]]:
        """
        Approach: BackTracking
        T: O(9!)
        S: O(81)
        :param board:
        :return:
        """
        def could_place(digit: int, row: int, col: int):

            return not (digit in rows[row] or digit in cols[col] or digit in boxes[box_index(row, col)])

        def place_number(digit: int, row: int, col: int):
            rows[row][digit] += 1
            cols[col][digit] += 1
            boxes[box_index(row, col)] += 1
            board[row][col] = str(digit)

        def place_next_number(row: int, col: int):
            nonlocal is_sudoku_solved
            if row == N - 1 and col == N - 1:
                is_sudoku_solved = True
            else:
                if col == N - 1:
                    backtrack(row + 1, 0)
                else:
                    backtrack(row, col + 1)

        def remove_number(digit: int, row: int, col: int):

            del rows[row][digit]
            del cols[col][digit]
            del boxes[box_index(row, col)][digit]
            board[row][col] = '.'

        def backtrack(row: int = 0, col: int = 0):
            if board[row][col] == '.':
                for num in range(1, 10):
                    if could_place(num, row, col):
                        place_number(num, row, col)
                        place_next_number(row, col)

                        if not is_sudoku_solved:
                            remove_number(num, row, col)
            else:
                place_next_number(row, col)

        n = 3
        N = n * n

        box_index = lambda r, c: (r // n) * n + (c // n)
        rows = [defaultdict(int) for _ in range(N)]
        cols = [defaultdict(int) for _ in range(N)]
        boxes = [defaultdict(int) for _ in range(N)]

        for row in range(N):
            for col in range(N):
                if board[row][col] != '.':
                    # fill all the existing number into rows, cols and boxes map
                    digit = ord(board[row][col]) - ord('0')
                    place_number(digit, row, col)
        is_sudoku_solved = False
        backtrack(0, 0)
