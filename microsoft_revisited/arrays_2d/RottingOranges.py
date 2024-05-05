from typing import List, Deque, Tuple
from collections import deque


class RottingOranges:

    def oranges_rotten_v1(self, grid: List[List[int]]):
        """
        Approach: In-place without using queue
        T: O(N ^ 2M ^ 2)
        S: O(1)
        :param grid:
        :return:
        """

        rows: int = len(grid)
        cols: int = len(grid[0])
        time_stamp: int = 2
        directions: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int], Tuple[int, int]] = (
            (0, 1), (1, 0), (0, -1), (-1, 0))

        def perform_rotting_process(timestamp: int) -> bool:

            traverse_grid: bool = False
            for row in range(rows):
                for col in range(cols):

                    if grid[row][col] == timestamp:
                        for direction in directions:
                            dr: int = row + direction[0]
                            dc: int = col + direction[1]

                            if 0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] == 1:
                                grid[dr][dc] = timestamp + 1
                                traverse_grid = True
            return traverse_grid

        while perform_rotting_process(time_stamp):
            time_stamp += 1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        return time_stamp - 2

    def oranges_rotten_v0(self, grid: List[List[int]]):
        """
        Approach: BFS
        T: O(NM)
        S: O(NM)
        :param grid:
        :return:
        """

        fresh_oranges: int = 0
        rows: int = len(grid)
        cols: int = len(grid[0])
        queue: Deque[Tuple[int, int]] = deque()
        minutes_elapsed: int = -1
        directions: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int], Tuple[int, int]] = (
            (0, 1), (1, 0), (0, -1), (-1, 0))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh_oranges += 1
                elif grid[row][col] == 2:
                    queue.append((row, col))

        # if no rotten oranges or fresh oranges
        if not queue and not fresh_oranges:
            return 0

        while queue:
            size: int = len(queue)
            minutes_elapsed += 1
            for _ in range(size):

                row, col = queue.popleft()
                for direction in directions:
                    dr: int = row + direction[0]
                    dc: int = col + direction[1]

                    if 0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] == 1:
                        grid[dr][dc] = 2
                        fresh_oranges -= 1
                        queue.append((dr, dc))
        return minutes_elapsed if fresh_oranges == 0 else -1
