from typing import List


class MinimumPathSum:

    def min_path_sum(self, grid: List[List[int]]) -> int:
        """
        Approach: DP
        t: O(N)
        S: O(1)
        :param grid:
        :return:
        """

        rows = len(grid)
        cols = len(grid[0])

        for col in range(1, cols):
            grid[0][col] += grid[0][col - 1]

        for row in range(1, rows):
            grid[row][0] += grid[row - 1][0]

        for row in range(1, rows):
            for col in range(1, cols):
                grid[row][col] += min(grid[row - 1][col], grid[row][col - 1])
        return grid[-1][-1]
