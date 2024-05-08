from typing import List


class RotateImage:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Approach: Transpose and Reflect
        T: O(MN)
        S: O(1)
        :param matrix:
        :return:
        """

        self._transpose(matrix)
        self._reflect(matrix)

    def _transpose(self, matrix: List[List[int]]) -> None:

        n = len(matrix)

        for row in range(n):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    def reflect(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for row in range(n):
            for col in range(n // 2):
                matrix[row][col], matrix[row][n - col - 1] = matrix[row][n - col - 1], matrix[row][col]
