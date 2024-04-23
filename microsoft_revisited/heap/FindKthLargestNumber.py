from heapq import heappop, heappush
from typing import List


class KthLargestNumber:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Approach: Heap
        T: O(log N)
        S: O(N)
        :param nums:
        :param k:
        :return:
        """

        minHeap = []

        for num in nums:
            heappush(minHeap, num)
            if len(minHeap) > k:
                heappop(minHeap)
        return minHeap[0]
