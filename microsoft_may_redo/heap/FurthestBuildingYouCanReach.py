from typing import List
from heapq import heappop, heappush


class Building:

    def furthest_you_can_reach(self, heights: List[int], bricks: int, ladder: int) -> int:
        """
        Approach: Heap
        T: O(N log N)
        S: O(N)
        :param heights:
        :param bricks:
        :param ladder:
        :return:
        """

        brick_allocations = []

        for i in range(len(heights) - 1):

            climb = heights[i + 1] - heights[i]

            if climb <= 0:
                continue

            heappush(brick_allocations, - climb)
            bricks -= climb

            if bricks < 0 and ladder == 0:
                return i

            if bricks < 0:
                bricks += -heappop(brick_allocations)
                ladder -= 1
        return len(heights) - 1
