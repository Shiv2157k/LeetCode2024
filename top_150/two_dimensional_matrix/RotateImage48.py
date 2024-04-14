from pprint import pprint
from typing import List


class RotateImage:

    def rotate(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Approach: Transpose and Reflect
        T: O(MN)
        S: O(NM)
        :param matrix:
        :return:
        """
        self._transpose(matrix)
        self._reflect(matrix)
        return matrix

    def _transpose(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for row in range(n):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    def _reflect(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for row in range(n):
            for col in range(n // 2):
                matrix[row][col], matrix[row][n - col - 1] = matrix[row][n - col - 1], matrix[row][col]


if __name__ == "__main__":
    rotateImage = RotateImage()
    pprint(rotateImage.rotate(
        [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    ))
