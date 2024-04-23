from typing import List
from collections import deque


class Islands:

    def totalNumberV1(self, grid: List[List[str]]) -> int:
        """
        Approach: DFS
        T: O()
        S: O()
        :param grid:
        :return:
        """
        rows, cols = len(grid), len(grid[0])

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        totalIslands = 0

        def depthFirstSearch(r: int, c: int):

            for direction in directions:
                dr = r + direction[0]
                dc = c + direction[1]

                if 0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] == '1':
                    grid[dr][dc] = '0'
                    depthFirstSearch(dr, dc)
                    grid[dr][dc] = '1'

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    totalIslands += 1
                    depthFirstSearch(row, col)
        return totalIslands

    def totalNumberV0(self, grid: List[List[str]]) -> int:
        """
        Approach: BFS
        T: O()
        S: O()
        :param grid:
        :return:
        """

        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        totalIslands = 0

        def breadthFirstSearch(row: int, col: int):

            queue = deque([(row, col)])

            while queue:

                r, c = queue.popleft()
                for direction in directions:
                    dr = r + direction[0]
                    dc = c + direction[1]

                    if 0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] == '1':
                        grid[dr][dc] = '0'
                        queue.append((dr, dc))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    totalIslands += 1
                    breadthFirstSearch(row, col)
        return totalIslands
