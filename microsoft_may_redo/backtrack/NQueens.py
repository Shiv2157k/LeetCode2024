from typing import List, Set


class NQueens:

    def solve_n_queens(self, n: int) -> List[List[int]]:
        """
        Approach: Back Tracking
        T: O(N!)
        S: O(N^2)
        :param n:
        :return:
        """

        def create_board(state: List[List[str]]) -> List[str]:
            board = []
            for row in state:
                board.append(''.join(row))
            return board

        def backtrack(row: int, cols: Set, diagonals: Set, anti_diagonals: Set, state: List[List[str]]):

            if row == n:
                ans.append(create_board(state))
                return

            for col in range(n):

                curr_diagonal = row + col
                curr_anti_diagonal = row - col

                if col in cols or curr_diagonal in diagonals or curr_anti_diagonal in anti_diagonals:
                    continue

                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)
                cols.add(col)
                state[row][col] = 'Q'
                backtrack(row + 1, cols, diagonals, anti_diagonals, state)
                diagonals.discard(curr_diagonal)
                anti_diagonals.discard(curr_anti_diagonal)
                cols.discard(col)
                state[row][col] = '.'

        ans = []
        empty_board = [['.'] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), empty_board)
        return ans
