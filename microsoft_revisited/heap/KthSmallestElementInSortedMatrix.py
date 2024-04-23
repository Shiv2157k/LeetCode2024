from heapq import heappop, heappush
from typing import List


class SortedMatrix:

    def kth_smallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Approach: Min Heap
        T: O(log N)
        S: O(N)
        :param matrix:
        :param k:
        :return:
        """
        min_heap: List[int] = []
        cols: int = len(matrix[0])
        rows: int = len(matrix)

        # push all the elements in first column
        for row in range(rows):
            heappush(min_heap, (matrix[row][0], row, 0))

        # iterate over k and pop out will gives the ksmallest
        k_smallest: int = 0
        while k:
            k_smallest, row, col = heappop(min_heap)
            if col + 1 < cols:
                heappush(min_heap, (matrix[row][col + 1], row, col + 1))
            k -= 1
        return k_smallest
