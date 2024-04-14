from typing import List
from collections import deque


class Islands:

    def totalNumberOfIslandsV1(self, grid: List[List[str]]) -> int:
        """
        BFS
        T: O(M * N)
        S: O(M * N)
        :param grid:
        :return:
        """
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        totalIslands = 0

        def bfs(row: int, col: int):

            queue = deque()
            queue.append((row, col))
            while queue:
                r, c = queue.popleft()

                for direction in directions:
                    dr = r + direction[0]
                    dc = c + direction[1]

                    if 0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] == "1":
                        grid[dr][dc] = "0"
                        queue.append((dr, dc))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    totalIslands += 1
                    bfs(row, col)

        return totalIslands

    def totalNumberOfIslandsV0(self, grid: List[List[str]]) -> int:
        """
        DFS
        T: O(M * N)
        S: O(M * N)
        :param grid:
        :return:
        """
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        totalIslands = 0

        def dfs(row: int, col: int) -> None:

            for direction in directions:
                dr = row + direction[0]
                dc = col + direction[1]

                if 0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] == "1":
                    grid[dr][dc] = "0"
                    dfs(dr, dc)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    totalIslands += 1
                    dfs(row, col)
        return totalIslands
