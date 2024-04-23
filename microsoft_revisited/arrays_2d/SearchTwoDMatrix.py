from typing import List


class SearchMatrix:

    def searchV1(self, matrix: List[List[int]], target: int) -> bool:
        """
        Approach: Binary Search
        T: O(log(mn))
        S: O(1)
        :param matrix:
        :param target:
        :return:
        """

        rows, cols = len(matrix), len(matrix[0])
        if rows == 0:
            return False

        left, right = 0, (rows * cols) - 1

        while left <= right:

            pivotIndex = left + (right - left) // 2
            row = pivotIndex // cols
            col = pivotIndex % cols
            pivotVal = matrix[row][col]

            if target > pivotVal:
                left = pivotIndex + 1
            elif target < pivotVal:
                right = pivotIndex - 1
            else:
                return True
        return False

    def searchV0(self, matrix: List[List[int]], target: int) -> bool:
        """
        Approach: Pruning
        T: O(M + N)
        S: O(1)
        :param matrix:
        :param target:
        :return:
        """

        rows, cols = len(matrix), len(matrix[0])
        row = rows - 1
        col = 0

        while row >= 0 and col < cols:
            if target < matrix[row][col]:
                row -= 1
            elif target > matrix[row][col]:
                col += 1
            else:
                return True
        return False
