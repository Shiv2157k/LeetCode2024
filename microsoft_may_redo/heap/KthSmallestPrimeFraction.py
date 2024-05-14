from heapq import heappop, heappush
from typing import List


class PrimeFraction:

    def kth_smallest(self, arr: List[int], k: int) -> List[int]:
        """
        Approach: Heapq
        T: O(N + K * log n)
        S: O(N)
        :param arr:
        :param k:
        :return:
        """

        min_heap = []

        for i in range(len(arr)):
            heappush(min_heap, ((arr[i] / arr[-1]), i, len(arr) - 1))

        for _ in range(k - 1):
            _, numerator_ptr, denominator_ptr = heappop(min_heap)
            denominator_ptr -= 1
            if denominator_ptr > numerator_ptr:
                heappush(min_heap, ((arr[numerator_ptr] / arr[denominator_ptr]), numerator_ptr, denominator_ptr))

        _, numerator_ptr, denominator_ptr = heappop(min_heap)
        return [arr[numerator_ptr], arr[denominator_ptr]]