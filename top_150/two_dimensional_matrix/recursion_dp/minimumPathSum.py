from typing import List


class Board:

    def minimumPathSumV0(self, grid: List[List[int]]) -> int:
        """
        Approach: DP
        T: O(M * N)
        S: O(N)
        :param grid:
        :return:
        """

        rows, cols = len(grid), len(grid[0])
        dp = [0] * cols

        for row in range(rows):
            for col in range(cols):
                if row == 0 and col != 0:
                    dp[col] = grid[row][col] + dp[col - 1]
                elif col == 0 and row != 0:
                    dp[col] = grid[row][col] + dp[col]
                elif col != 0 and row != 0:
                    dp[col] = grid[row][col] + min(dp[col], dp[col - 1])
                else:
                    dp[col] = grid[row][col]
        return dp[cols - 1]

    def minimumPathSumV1(self, grid: List[List[int]]) -> int:
        """
        Approach: DP in place
        T: O(M * N)
        S: O(1)
        :param grid:
        :return:
        """

        rows, cols = len(grid), len(grid[0])

        for row in range(1, rows):
            grid[row][0] += grid[row - 1][0]

        for col in range(1, cols):
            grid[0][col] += grid[0][col - 1]

        for row in range(1, rows):
            for col in range(1, cols):
                grid[row][col] += min(grid[row][col - 1], grid[row - 1][col])
        return grid[rows - 1][cols - 1]


if __name__ == "__main__":
    board = Board()
    print(board.minimumPathSumV0(
        [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    ))
    print(board.minimumPathSumV0(
        [[1, 2, 3], [4, 5, 6]]
    ))
    print(board.minimumPathSumV1(
        [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    ))
    print(board.minimumPathSumV1(
        [[1, 2, 3], [4, 5, 6]]
    ))
