from typing import Set


class NQueensII:

    def total_n_queens(self, n: int) -> int:
        """
        Approach: Backtrack
        T: O(N!)
        S: O(N)
        :param n:
        :return:
        """

        def backtrack(row: int, cols: Set, diagonals: Set, anti_diagonals: Set):
            nonlocal distinct_sol
            if row == n:
                distinct_sol += 1
                return

            for col in range(n):

                curr_diagonals = row + col
                curr_anti_diagonals = row - col

                if col in cols or curr_diagonals in diagonals or curr_anti_diagonals in anti_diagonals:
                    continue

                cols.add(col)
                diagonals.add(curr_diagonals)
                anti_diagonals.add(curr_anti_diagonals)
                backtrack(row + 1, cols, diagonals, anti_diagonals)
                cols.discard(col)
                diagonals.discard(curr_diagonals)
                anti_diagonals.discard(curr_anti_diagonals)

        distinct_sol = 0
        backtrack(0, set(), set(), set())
        return distinct_sol
