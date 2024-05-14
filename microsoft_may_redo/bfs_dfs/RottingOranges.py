from typing import List
from collections import deque


class RottingOranges:

    def oranges_rotting_v1(self, grid: List[List[int]]) -> int:
        """
        Approach: BFS without queue
        T: O(M^2N^2)
        S: O(1)
        :param grid:
        :return:
        """

        rows, cols = len(grid), len(grid[0])
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def perform_rotting_process(ts: int) -> bool:
            traverse_grid = False
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] == ts:
                        for direction in directions:
                            dr = row + direction[0]
                            dc = col + direction[1]

                            if 0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] == 1:
                                grid[dr][dc] = ts + 1
                                traverse_grid = True
            return traverse_grid

        time_stamp = 2
        while perform_rotting_process(time_stamp):
            time_stamp += 1
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        return time_stamp - 2

    def oranges_rotting_v0(self, grid: List[List[int]]) -> int:
        """
        Approach: BFS using Queue
        T: O(MN)
        S: O(N)
        :param grid:
        :return:
        """

        rows = len(grid)
        cols = len(grid[0])
        fresh_oranges = 0
        queue = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh_oranges += 1
                elif grid[row][col] == 2:
                    queue.append((row, col))
        # offset
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        minutes_elapsed = 0
        while queue:
            level = len(queue)
            minutes_elapsed += 1
            for _ in range(level):
                row, col = queue.popleft()
                for direction in directions:
                    dr = row + direction[0]
                    dc = col + direction[1]
                    if 0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] == 1:
                        grid[row][col] = 2
                        queue.append((row, col))
                        fresh_oranges -= 1
        return minutes_elapsed if fresh_oranges == 0 else -1
