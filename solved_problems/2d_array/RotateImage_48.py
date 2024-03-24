from typing import List
from pprint import pprint


class RotateImage:

    def rotate(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Approach: Transpose and Reflect
        T: O(M)
        S: O(1)
        :param matrix:
        :return:
        """
        matrix = self._transpose(matrix)
        matrix = self._reflect(matrix)
        return matrix

    def _transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)

        for row in range(n):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        return matrix

    def _reflect(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)

        for row in range(n):
            for col in range(n // 2):
                matrix[row][col], matrix[row][n - col - 1] = matrix[row][n - col - 1], matrix[row][col]
        return matrix


if __name__ == "__main__":
    rotateImage = RotateImage()
    pprint(rotateImage.rotate(
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
    ))
