from typing import List
from heapq import heappop, heappush


class Buildings:

    def furthest_to_reach(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        Approach: Heap
        T: O(N log N)
        S: O(N)
        :param heights:
        :param bricks:
        :param ladders:
        :return:
        """

        brick_allocation: List[int] = []

        for i in range(len(heights) - 1):

            climb = heights[i + 1] - heights[i]

            if climb < 0:
                continue

            heappush(brick_allocation, -climb)
            bricks -= climb

            if bricks < 0 and ladders == 0:
                return i

            if bricks < 0:
                bricks += -heappop(brick_allocation)
                ladders -= 1
        return len(heights) - 1
