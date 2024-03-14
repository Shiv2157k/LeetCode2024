from typing import List


class Island:

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        Approach: Better Counting
        T: O(MN)
        S: O(1)
        :param grid:
        :return:
        """
        rows, cols = len(grid), len(grid[0])
        perimeter = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4

                    # up
                    if r > 0 and grid[r - 1][c] == 1:
                        perimeter -= 2
                    # left
                    if c > 0 and grid[r][c - 1] == 1:
                        perimeter -= 2
        return perimeter

    def islandPerimeter_(self, grid: List[List[int]]) -> int:
        """
        Approach: Simple Counting
        T: O(MN)
        S: O(1)
        :param grid:
        :return:
        """
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        for r in range(rows):
            for c in range(cols):

                # if it is a land
                if grid[r][c] == 1:
                    # up
                    if r == 0:
                        up = 0
                    else:
                        up = grid[r - 1][c]
                    # left
                    if c == 0:
                        left = 0
                    else:
                        left = grid[r][c - 1]
                    # right
                    if c == cols - 1:
                        right = 0
                    else:
                        right = grid[r][c + 1]
                    # down
                    if r == rows - 1:
                        down = 0
                    else:
                        down = grid[r + 1][c]
                    perimeter += 4 - (up + left + right + down)
        return perimeter


if __name__ == "__main__":
    island = Island()
    print(island.islandPerimeter_([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
    print(island.islandPerimeter_([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
