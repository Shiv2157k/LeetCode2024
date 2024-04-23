from typing import List


class RotateImage:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Approach: Transpose and Reflect
        T: O(M * N)
        S: O(1)
        :param matrix:
        :return:
        """

        self.transpose(matrix)
        self.reflect(matrix)

    def transpose(self, matrix: List[List[int]]) -> None:

        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(row + 1, cols):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    def reflect(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            for col in range(cols // 2):
                matrix[row][col], matrix[row][cols - col - 1] = matrix[row][cols - col - 1], matrix[row][col]
