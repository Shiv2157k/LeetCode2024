from typing import List


class TwoDimensionalMatrix:

    def searchMatrixV1(self, matrix: List[List[int]], target: int) -> bool:
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

        left, right = 0, rows * cols - 1

        while left <= right:

            pivotIndex = left + (right - left) // 2
            row = pivotIndex // cols
            col = pivotIndex % cols
            pivotElement = matrix[row][col]

            if target < pivotElement:
                right = pivotIndex - 1
            elif target > pivotElement:
                left = pivotIndex + 1
            else:
                return True
        return False

    def searchMatrixV0(self, matrix: List[List[int]], target: int) -> bool:
        """
        Approach: Pruning
        T: O(M + N)
        S: O(1)
        :param matrix:
        :param target:
        :return:
        """
        rows, cols = len(matrix), len(matrix[0])

        row, col = rows - 1, 0

        while row >= 0 and col < cols:

            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:
                return True
        return False


if __name__ == "__main__":
    twoDMatrix = TwoDimensionalMatrix()
    print(twoDMatrix.searchMatrixV0(
        [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3
    ))
    print(twoDMatrix.searchMatrixV1(
        [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3
    ))
    print(twoDMatrix.searchMatrixV0(
        [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13
    ))
    print(twoDMatrix.searchMatrixV1(
        [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13
    ))
