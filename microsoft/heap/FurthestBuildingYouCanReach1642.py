import heapq
from heapq import heappop, heappush
from typing import List


class Buildings:

    def furthestYouCanReachV0(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        Approach: Max Heap
        T: O(N log N) or O(N log B)
        S: O(N) or O(B)
        :param heights:
        :param bricks:
        :param ladders:
        :return:
        """
        # this will be our max heap
        brickAllocations = []

        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]

            if climb <= 0:
                continue

            heappush(brickAllocations, -climb)
            bricks -= climb

            if bricks < 0 and ladders == 0:
                return i

            if bricks < 0:
                bricks += -heappop(brickAllocations)
                ladders -= 1
        return len(heights) - 1

    def furthestYouCanReachV1(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        Approach: Min Heap
        T: O(N log N) or O(N log L)
        S: O(N) or O(L)
        :param heights:
        :param bricks:
        :param ladders:
        :return:
        """
        # this will be the min Heap
        ladderAllocations = []

        # considering we compare two adjacent buildings together range -> len(heights) - 1
        for i in range(len(heights) - 1):

            climb = heights[i + 1] - heights[i]

            # if there is no climb simply move to next building
            if climb <= 0:
                continue

            heapq.heappush(ladderAllocations, climb)

            # if the total ladders used is under ladders provided
            # simply move to next building
            if len(ladderAllocations) <= ladders:
                continue

            bricks -= heappop(ladderAllocations)

            # there is no way we can go to the next building
            if bricks < 0:
                return i

        # we came this for we reached to final building
        return len(heights) - 1
