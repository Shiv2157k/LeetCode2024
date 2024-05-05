from typing import List, Tuple, Set


class Island:

    def max_area(self, grid: List[List[int]]) -> int:
        """
        Approach: DFS Iterative with stack
        T: O(M * N)
        S: O(M * N)
        :param grid:
        :return:
        """

        rows: int = len(grid)
        cols: int = len(grid[0])
        directions: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int], Tuple[int, int]] = (
            (0, 1), (1, 0), (-1, 0), (0, -1))

        visited: Set = set()
        max_area = 0

        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == 1 and (row, col) not in visited:
                    curr_area = 0
                    stack = [(row, col)]
                    visited.add((row, col))

                    while stack:
                        r, c = stack.pop()

                        for direction in directions:
                            dr = r + direction[0]
                            dc = c + direction[1]

                            if 0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] == 1 and (dr, dc) not in visited:
                                curr_area += 1
                                visited.add((dr, dc))
                                stack.append((dr, dc))
                    if max_area < curr_area:
                        max_area = curr_area
        return max_area
