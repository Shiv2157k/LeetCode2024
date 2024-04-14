from typing import List, Set


class NQueensII:

    def totalDistinctWays(self, n: int) -> int:
        """
        Approach: Backtracking
        T: O(N!)
        S: O(N)
        :param n:
        :return:
        """

        def backtrack(row: int, diagonals: Set, antiDiagonals: Set, cols: Set):
            nonlocal distinctWays
            # base case
            if row == n:
                distinctWays += 1
                return

            for col in range(n):

                currDiagonal = row + col
                currAntiDiagonal = row - col

                if col in cols or currDiagonal in diagonals or currAntiDiagonal in antiDiagonals:
                    continue

                cols.add(col)
                diagonals.add(currDiagonal)
                antiDiagonals.add(currAntiDiagonal)
                backtrack(row + 1, diagonals, antiDiagonals, cols)
                cols.remove(col)
                diagonals.remove(currDiagonal)
                antiDiagonals.remove(currAntiDiagonal)

        distinctWays = 0
        backtrack(1, set(), set(), set())
        return distinctWays
