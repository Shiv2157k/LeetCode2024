from typing import List


class Islands:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Approach: DFS with iterative stack
        T: O(N * M)
        S: O(N * M)
        :param grid:
        :return:
        """

        rows, cols = len(grid), len(grid[0])
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
        visited = set()
        maxArea = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    currArea = 0
                    stack = [(row, col)]
                    visited.add((row, col))

                    while stack:
                        r, c = stack.pop()
                        currArea += 1

                        for direction in directions:

                            dr = r + direction[0]
                            dc = c + direction[1]

                            if 0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] == 1 and (dr, dc) not in visited:
                                stack.append((dr, dc))
                                visited.add((dr, dc))
                                
                    if currArea > maxArea:
                        maxArea = currArea
        return maxArea
