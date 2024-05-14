from typing import List


class Island:

    def max_area_of_an_island(self, grid: List[List[int]]) -> int:
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
        max_area = 0

        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == 1 and (row, col) not in visited:
                    stack = [(row, col)]
                    curr_area = 0
                    visited.add((row, col))

                    while stack:
                        r, c = stack.pop()
                        curr_area += 1

                        for direction in directions:
                            dr = r + direction[0]
                            dc = c + directions[1]

                            if 0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] == 1 and (dr, dc) not in visited:
                                stack.append((dr, dc))
                                visited.add((dr, dc))
                    if max_area < curr_area:
                        max_area = curr_area
        return max_area
