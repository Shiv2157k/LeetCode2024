from collections import deque
from typing import List


class Oranges:
    def oranges_rotting_time_v1(self, grid: List[List[int]]) -> int:
        """
        Approach: BFS with no queue
        T: O(M^2 N^2)
        S: O(1)
        :param grid:
        :return:
        """
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def processRottingOranges(timestamp: int) -> bool:
            is_next_level = False
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] == timestamp:
                        for direction in directions:
                            dr = row + direction[0]
                            dc = col + direction[1]
                            if 0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] == 1:
                                grid[dr][dc] = timestamp + 1
                                is_next_level = True
            return is_next_level

        timestamp = 2
        while processRottingOranges(timestamp):
            timestamp += 1

        # provide the minutes elapsed before check if there are any fresh oranges
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        return timestamp - 2

    def oranges_rotting_time(self, grid: List[List[int]]) -> int:
        """
        Approach: DFS - queue
        Time Complexity: O(MN)
        Space Complexity: O(N)
        :param grid:
        :return:
        """

        # Step 1:
        # - queue all the level 1 rotting oranges into the queue
        # - calculate all the fresh oranges in the grid helpful at the end.
        fresh_oranges = 0
        queue = deque()
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_oranges += 1

        # mark the end of the level in the queue to skip using the visited set
        queue.append((-1, -1))

        minutes_elapsed = -1
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Step 2: run over the queue level by level and mark the rotting oranges
        while queue:
            row, col = queue.popleft()
            # if we have reached a level
            if row == -1:  # we have completed one stage/ level
                minutes_elapsed += 1
                if queue:  # if there are still nodes/ grids to explore mark this level
                    queue.append((-1, -1))
            else:  # performing rotting process
                for direction in directions:
                    dr = row + direction[0]
                    dc = col + direction[1]
                    # to make sure we are within the boundaries
                    if 0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] == 1:
                        fresh_oranges -= 1
                        grid[dr][dc] = 2
                        # add the next level grids
                        queue.append((dr, dc))
        return minutes_elapsed if fresh_oranges == 0 else -1


if __name__ == "__main__":
    oranges = Oranges()
    print(oranges.oranges_rotting_time(
        [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    ))
    print(oranges.oranges_rotting_time(
        [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    ))
    print(oranges.oranges_rotting_time(
        [[0, 2]]
    ))
    print(oranges.oranges_rotting_time_v1(
        [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    ))
    print(oranges.oranges_rotting_time_v1(
        [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    ))
    print(oranges.oranges_rotting_time_v1(
        [[0, 2]]
    ))
