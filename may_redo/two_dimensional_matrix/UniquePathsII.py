from typing import List


class UniquePathII:

    def total_unique_paths(self, obstacle_grid: List[List[int]]) -> int:
        """
        Approach: DP
        T: O(NM)
        S: O(1)
        :param obstacle_grid:
        :return:
        """

        # flip the obstacle grid from 1 to 0
        # and non obstacle grid from 0 to 1
        rows = len(obstacle_grid)
        cols = len(obstacle_grid[0])

        if obstacle_grid[0][0] == 1:
            return 0
        obstacle_grid[0][0] = 1

        for row in range(1, rows):
            if obstacle_grid[row][0] == 0:
                obstacle_grid[row][0] = obstacle_grid[row - 1][0]
            else:
                obstacle_grid[row][0] = 0

        for col in range(1, cols):
            if obstacle_grid[0][col] == 0:
                obstacle_grid[0][col] = obstacle_grid[0][col - 1]
            else:
                obstacle_grid[0][col] = 0

        for row in range(1, rows):
            for col in range(1, cols):
                if obstacle_grid[row][col] == 0:
                    obstacle_grid[row][col] = obstacle_grid[row - 1][col] + obstacle_grid[row][col - 1]
                else:
                    obstacle_grid[row][col] = 0
        return obstacle_grid[rows - 1][cols - 1]
