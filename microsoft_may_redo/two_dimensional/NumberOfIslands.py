from typing import List
from collections import deque


class Islands:

    def number_of_islands_v0(self, grid: List[List[int]]) -> int:

        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
        rows = len(grid)
        cols = len(grid[0])
        total_islands = 0

        def backtrack(r: int, c: int):
            for direction in directions:
                dr = r + direction[0]
                dc = c + direction[1]
                if 0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] == '1':
                    grid[dr][dc] = '0'
                    backtrack(dr, dc)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    total_islands += 1
                    backtrack(row, col)
        return total_islands

    def number_of_islands_v1(self, grid: List[List[int]]) -> int:
        """
        Approach: BFS
        T: O(M * N)
        S: O(min(M,N))
        :param grid:
        :return:
        """
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
        total_islands = 0
        rows = len(grid)
        cols = len(grid[0])

        def breadth_first_search(r: int, c: int):

            queue = deque([(r, c)])

            while queue:
                curr_row, curr_col = queue.popleft()

                for direction in directions:
                    dr = curr_row + direction[0]
                    dc = curr_col + direction[1]

                    if 0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] == '1':
                        grid[dr][dc] = '0'
                        queue.append((dr, dc))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    total_islands += 1
                    breadth_first_search(row, col)
        return total_islands
