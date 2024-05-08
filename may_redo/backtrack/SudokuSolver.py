from typing import List
from collections import defaultdict


class SudokuSolver:

    def solve_sudoku(self, board: List[List[str]]) -> None:
        """
        Approach:
        T: O()
        S: O()
        :param board:
        :return:
        """

        def could_place(num: int, row: int, col: int):
            return not (num in rows[row] or num in cols[col] or num in boxes[box_idx(row, col)])

        def place_number(num: int, row: int, col: int):
            rows[row][num] += 1
            cols[col][num] += 1
            boxes[box_idx(row, col)][num] += 1
            board[row][col] = str(num)

        def place_next_number(num: int, row: int, col: int):
            nonlocal sudoku_solved
            if row == N - 1 and col == N - 1:
                sudoku_solved = True
            else:
                if col == N - 1:
                    backtrack(row + 1, 0)
                else:
                    backtrack(row, col + 1)

        def remove_number(num: int, row: int, col: int):
            del rows[row][num]
            del cols[col][num]
            del boxes[box_idx(row, col)][num]
            board[row][col] = '.'

        def backtrack(row: int, col: int):
            if board[row][col] == '.':
                for num in range(1, 10):
                    if could_place(num, row, col):
                        place_number(num, row, col)
                        place_next_number(row, col)

                        if not sudoku_solved:
                            remove_number(num, row, col)
            else:
                place_next_number(row, col)

        n = 3
        N = n * n

        box_idx = lambda r, c: (r // n) * n + (c // n)

        rows = [defaultdict(int) for _ in range(N)]
        cols = [defaultdict(int) for _ in range(N)]
        boxes = [defaultdict(int) for _ in range(N)]

        for row in range(N):
            for col in range(N):

                if board[row][col].isnumeric():
                    digit = int(board[row][col])
                    place_number(digit, row, col)

        sudoku_solved = False
        backtrack(0, 0)
