from typing import List, Tuple
from heapq import heappop, heappush


class KthSortedElement:

    def find_in_matrix_v1(self, matrix: List[List[int]], k: int) -> int:

        def binary_search(low: int, mid: int, high: int) -> Tuple[int, int, int]:

            row, col = len(matrix) - 1, 0
            count = 0

            while row > 0 and col < len(matrix):
                if matrix[row][col] > mid:
                    high = min(high, matrix[row][col])
                    row -= 1
                else:
                    low = max(low, matrix[row][col])
                    count = count + row + 1
                    col += 1
            return count, low, high

        left = matrix[0][0]
        right = matrix[-1][-1]

        while left < right:

            low, high = matrix[0][0], matrix[-1][-1]
            mid = left + (right - left) // 2

            count, low, high = binary_search(low, mid, high)

            if count == k:
                return low
            elif count < k:
                left = high
            else:
                right = mid
        return left

    def find_in_matrix_v0(self, matrix: List[List[int]], k: int) -> int:
        """
        Approach: Min Heap
        T: O(X + K log X)
        S: O(X)
        :param matrix:
        :param k:
        :return:
        """

        rows = len(matrix)
        cols = len(matrix[0])
        min_heap = []

        for row in range(rows):
            heappush(min_heap, (matrix[row][0], row, 0))

        k_smallest = int
        while k:
            k_smallest, row, col = heappop(min_heap)
            if col + 1 < cols:
                heappush(min_heap, (matrix[row][col + 1], row, col + 1))
            k -= 1
        return k_smallest
