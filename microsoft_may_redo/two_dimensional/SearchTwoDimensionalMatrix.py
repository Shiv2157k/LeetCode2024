from typing import List


class Matrix:

    def search_v0(self, matrix: List[List[int]], target: int) -> bool:
        """
        Approach: Binary Search
        T: O(log n!)
        S: O(1)
        :param matrix:
        :param target:
        :return:
        """

        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        rows = len(matrix)
        cols = len(matrix[0])

        for index in range(min(rows, cols)):
            has_target_in_vertical = 0
            has_target_in_horizontal = 0

            if has_target_in_vertical or has_target_in_horizontal:
                return True
        return False

    def __binary_search(self, target: int, matrix: List[List[int]], left: int, right: int, is_vertical: bool) -> bool:

        pointer = left

        while pointer <= right:

            pivot = pointer + (right - pointer) // 2

            if is_vertical:
                if matrix[pivot][left] < target:
                    pointer = pivot + 1
                elif matrix[pivot][left] > target:
                    right = pivot - 1
                else:
                    return True
            else:
                if matrix[left][pivot] < target:
                    pointer = pivot + 1
                elif matrix[left][pivot] > target:
                    right = pivot - 1
                else:
                    return True
        return False

    def search_v1(self, matrix: List[List[int]], target: int) -> bool:
        """
        Approach: Pruning
        T: O(N + M)
        S: O(1)
        :param matrix:
        :param target:
        :return:
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        row = rows - 1
        col = 0

        while row >= 0 and col < cols:

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row -= 1
            else:
                col += 1
        return False
