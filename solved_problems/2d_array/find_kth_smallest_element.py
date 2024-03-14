import heapq
from typing import List

class Matrix:

    def binarySearch(self, matrix: List[List[int]], mid: int, smaller: int, larger: int) -> (int, int, int):

        count = 0
        n = len(matrix)
        row, col = n - 1, 0

        while row >= 0 and col < n:

            if mid < matrix[row][col]:
                larger = min(larger, matrix[row][col])
                row -= 1
            else:
                smaller = max(smaller, matrix[row][col])
                col += 1
                count += row + 1
        return count, smaller, larger

    def findKthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Approach: Binary Search
        :param matrix:
        :param k:
        :return:
        """

        start, end = matrix[0][0], matrix[-1][-1]

        while start < end:
            smaller, larger = matrix[0][0], matrix[-1][-1]
            mid = start + (end - start) // 2
            count, smaller, larger = self.binarySearch(matrix, mid, smaller, larger)
            if count == k:
                return start
            if count < k:
                start = larger
            else:
                end = smaller
        return start

    def find_kth_smallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Approach: Heap
        :param matrix:
        :param k:
        :return:
        """
        element = 0
        minHeap = []
        N = len(matrix)
        for row in range(min(N, k)):
            heapq.heappush(minHeap, (matrix[row][0], row, 0))

        while k:

            element, row, col = heapq.heappop(minHeap)

            if col < N - 1:
                heapq.heappush(minHeap, (matrix[row][col + 1], row, col + 1))
            k -= 1
        return element


if __name__ == "__main__":
    matrix = Matrix()
    print(matrix.find_kth_smallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
    print(matrix.findKthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
