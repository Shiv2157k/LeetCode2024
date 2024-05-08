from typing import List, Set


class NQueens:

    def solve(self, n: int) -> List[List[str]]:
        """
        Approach: Back Track
        T: O(N!)
        S: O(N^2)
        :param n:
        :return:
        """

        def create_board(state: List[List[str]]):
            valid_board = []
            for row in state:
                valid_board.append(''.join(row))
            return valid_board

        def backtrack(row: int, cols: Set[int], diagonals: Set[int], anti_diagonals: Set[int], state: List[List[str]]):

            # base case
            if row == n:
                output.append(create_board(state))
                return

            for col in range(n):

                curr_diagonal = row + col
                curr_anti_diagonal = row - col

                if curr_diagonal in diagonals or curr_anti_diagonal in anti_diagonals or col in cols:
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

        output = []
        empty_board = [['.'] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), empty_board)
        return output
