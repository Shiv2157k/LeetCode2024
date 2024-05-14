from typing import List


class RotateImage:

    def rotate(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Approach: Transpose and Reflect
        T: O(MN)
        S: O(MN)
        :param matrix:
        :return:
        """

        self.__transpose(matrix)
        self.__reflect(matrix)
        return matrix

    def __transpose(self, matrix: List[List[int]]) -> None:

        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(row + 1, cols):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    def __reflect(self, matrix: List[List[int]]) -> None:

        rows = len(matrix)
        cols = len(matrix)

        for row in range(rows):
            for col in range(cols // 2):
                matrix[row][col], matrix[row][cols - col - 1] = matrix[row][cols - col - 1], matrix[row][col]
