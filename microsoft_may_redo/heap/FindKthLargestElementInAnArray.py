import heapq
from typing import List
from heapq import heappop, heappush


class KthLargestElement:

    def find_kth_largest_v0(self, nums: List[int], k: int) -> int:
        """
        Approach: Heap
        T: O(n * log K)
        S: O(K)
        :param nums:
        :param k:
        :return:
        """

        min_heap = []

        for num in nums:

            heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]
