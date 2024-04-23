from typing import List


class MinimumPathSum:

    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Approach: DP
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
                grid[row][col] = grid[row][col] + min(grid[row - 1][col], grid[row][col - 1])
        return grid[rows - 1][cols - 1]
