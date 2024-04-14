from typing import List


class UniquePathsII:

    def getUniquePathsWithoutObstacle(self, obstacleGrid: List[List[int]]) -> int:
        """
        Approach: DP
        T: O(M * N)
        S: O(1)
        :param obstacleGrid:
        :return:
        """

        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        # validation if there is an obstacle on 1st grid
        if obstacleGrid[0][0] == 1:
            return 0

        # flip the first grid
        obstacleGrid[0][0] = 1

        # mark the first column or each row based on the obstacle present or not
        for row in range(1, rows):
            if obstacleGrid[row][0] == 0:
                obstacleGrid[row][0] = obstacleGrid[row - 1][0]
            else:
                obstacleGrid[row][0] = 0

        # mark all the columns of first row based on the obstacle present or not
        for col in range(1, cols):
            if obstacleGrid[0][col] == 0:
                obstacleGrid[0][col] = obstacleGrid[0][col - 1]
            else:
                obstacleGrid[0][col] = 0

        # traverse through remaining rows and cols basing the first column and row
        for row in range(1, rows):
            for col in range(1, cols):
                if obstacleGrid[row][col] == 0:
                    obstacleGrid[row][col] = obstacleGrid[row - 1][col] + obstacleGrid[row][col - 1]
                else:  # flip the obstacle to 0
                    obstacleGrid[row][col] = 0
        return obstacleGrid[rows - 1][cols - 1]


if __name__ == "__main__":
    paths = UniquePathsII()
    print(paths.getUniquePathsWithoutObstacle(
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    ))
