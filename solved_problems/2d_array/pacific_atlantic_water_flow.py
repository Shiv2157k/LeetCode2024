from collections import deque
from typing import List, Deque, Set


class WaterFlow:

    def in_both_pacific_and_atlantic_v0(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Approach: DFS
        T: O(N)
        S: O(N)
        :param heights:
        :return:
        """
        if len(heights) == 0 or len(heights[0]) == 0:
            return []

        rows, cols = len(heights), len(heights[0])

        pacific_reachable, atlantic_reachable = set(), set()
        both_reaches = []

        def depth_first_search(row: int, col: int, reachable: Set):

            reachable.add((row, col))

            for dr, dc in [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]:
                if dr < 0 or dc < 0 or dr >= rows or dc >= cols:
                    continue
                if (dr, dc) in reachable:
                    continue
                if heights[dr][dc] < heights[row][col]:
                    continue
                depth_first_search(dr, dc, reachable)

        for r in range(rows):
            depth_first_search(r, 0, pacific_reachable)
            depth_first_search(r, cols - 1, atlantic_reachable)

        for c in range(cols):
            depth_first_search(0, c, pacific_reachable)
            depth_first_search(rows - 1, c, atlantic_reachable)

        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific_reachable and (row, col) in atlantic_reachable:
                    both_reaches.append([row, col])
        return both_reaches

    def in_both_pacific_and_atlantic_v1(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Approach: BFS
        T: O(N)
        S: O(N)
        :param heights:
        :return:
        """
        if len(heights) == 0 or len(heights[0]) == 0:
            return []

        pacific_queue, atlantic_queue = deque(), deque()

        rows, cols = len(heights), len(heights[0])

        for row in range(rows):
            pacific_queue.append((row, 0))
            atlantic_queue.append((row, cols - 1))
        for col in range(cols):
            pacific_queue.append((0, col))
            atlantic_queue.append((rows - 1, col))

        def breadth_first_search(queue: Deque):
            reachable = set()
            while queue:
                r, c = queue.popleft()
                reachable.add((r, c))
                for dr, dc in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:

                    if dr < 0 or dc < 0 or dr >= rows or dc >= cols:
                        continue
                    if (dr, dc) in reachable:
                        continue
                    if heights[dr][dc] < heights[r][c]:
                        continue
                    queue.append((dr, dc))
            return reachable

        pacific_reachable = breadth_first_search(pacific_queue)
        atlantic_reachable = breadth_first_search(atlantic_queue)
        reaches_both = []

        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific_reachable and (row, col) in atlantic_reachable:
                    reaches_both.append([row, col])
        return reaches_both


if __name__ == "__main__":
    water_flow = WaterFlow()
    print(water_flow.in_both_pacific_and_atlantic_v1(
        [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    ))
    print(water_flow.in_both_pacific_and_atlantic_v0(
        [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    ))
