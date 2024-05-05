from typing import List


class TwoDimensionalMatrix:

    def search_vo(self, matrix: List[List[int]], target: int) -> bool:
        """
        Approach: Pruning
        T: O(M + N)
        S: O(1)
        :param matrix:
        :param target:
        :return:
        """

        rows = len(matrix)
        cols = len(matrix[0])
        row = rows - 1
        col = 0

        while row >= 0 and col < cols:

            if target < matrix[row][col]:
                row -= 1
            elif target > matrix[row][col]:
                col += 1
            elif target == matrix[row][col]:
                return True
        return False

    def search_v1(self, matrix: List[List[int]], target: int) -> bool:
        """
        Approach: Binary Search
        T: O(log(mn))
        S: O(1)
        :param matrix:
        :param target:
        :return:
        """

        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = (rows * cols) - 1

        while left <= right:

            pivot_ptr = left + (right - left) // 2
            row = pivot_ptr // cols
            col = pivot_ptr % cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = pivot_ptr - 1
            elif matrix[row][col] < target:
                left = pivot_ptr + 1
        return False

