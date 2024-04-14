from typing import List
from collections import deque



class WaterFlow:


    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Approach: DFS
        T: O(M * N)
        S: O(M * N)
        :param heights:
        :return:
        """

        if not heights or not heights[0]:
            return []

        pacificQueue, atlanticQueue = deque(), deque()
        rows, cols = len(heights), len(heights[0])

        for row in range(rows):
            pacificQueue.append((row, 0))
            atlanticQueue.append((row, cols - 1))

        for col in range(cols):
            pacificQueue.append((0, col))
            atlanticQueue.append((rows - 1, col))

        def breadthFirstSearch(queue):

            reachable = set()

            while queue:
                row, col = queue.popleft()
                reachable.add((row, col))
                for dr, dc in [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]:

                    if (dr, dc) in reachable:
                        continue

                    if dr < 0 or dr >= rows or dc < 0 or dc >= cols:
                        continue

                    if heights[dr][dc] < heights[row][col]:
                        continue

                    queue.append((dr, dc))
            return reachable

        pacificReachable = breadthFirstSearch(pacificQueue)
        atlanticReachable = breadthFirstSearch(atlanticQueue)
        bothWaterFlow = []

        for row in range(rows):
            for col in range(cols):

                if (row, col) in pacificReachable and (row, col) in atlanticReachable:
                    bothWaterFlow.append([row, col])
        return bothWaterFlow

    # ToDo: DFS later