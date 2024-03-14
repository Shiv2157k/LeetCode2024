from collections import deque
from typing import List


class Island:

    def total_islands_bfs(self, grid: List[List[str]]) -> str:
        """
        Approach: BFS
        T: O(M*N)
        S: O(M*N)
        :param grid:
        :return:
        """
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        count = 0

        def breadth_first_search(row: str, col: str):
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
                    count += 1
                    breadth_first_search(row, col)
        return count

    def total_islands_dfs(self, grid: List[List[str]]) -> int:
        """
        Approach: DFS
        T: O(M*N)
        S: O(M*N
        :param grid:
        :return:
        """

        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        count = 0

        def depth_first_search(row: str, col: str):

            for direction in directions:
                dr = row + direction[0]
                dc = col + direction[1]
                if 0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] == "1":
                    grid[dr][dc] = "0"
                    depth_first_search(dr, dc)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    count += 1
                    depth_first_search(row, col)
        return count


if __name__ == "__main__":
    island = Island()
    print(island.total_islands_dfs(
        [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    ))
    print(island.total_islands_dfs(
        [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
    ))

    print(island.total_islands_bfs(
        [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    ))
    print(island.total_islands_bfs(
        [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
    ))
