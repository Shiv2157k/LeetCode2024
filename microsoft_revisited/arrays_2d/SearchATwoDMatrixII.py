from typing import List


class TwoDimensionalMatrix:

    def searchMatrixV0(self, matrix: List[List[int]], target: int) -> bool:
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

        rows: int = len(matrix)
        cols: int = len(matrix[0])
        for index in range(min(rows, cols)):
            has_target_in_vertical = self._binary_search(target, matrix, index, rows - 1, True)
            has_target_in_horizontal = self._binary_search(target, matrix, index, cols - 1, False)

            if has_target_in_horizontal or has_target_in_vertical:
                return True
        return False

    def _binary_search(self, target: int, matrix: List[List[int]], left: int, right: int,
                       is_vertical: bool = False) -> bool:

        pointer: int = left

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

    def searchMatrixV1(self, matrix: List[List[int]], target: int) -> bool:
        """
        Approach: Pruning / Search Space Reduction
        T: O(M + N)
        S: O(1)
        :param matrix:
        :param target:
        :return:
        """
        if not matrix or len(matrix[0]) == 0 or len(matrix) == 0:
            return False

        rows, cols = len(matrix), len(matrix[0])
        row = len(matrix) - 1
        col = 0

        while col < cols and row >= 0:

            if matrix[row][col] < target:
                col += 1
            elif matrix[row][col] > target:
                row -= 1
            else:
                return True
        return False
