from typing import List


class Matrices:

    def setMatrixToZero(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Approach: In-place Traversal Without Extra Space
        T: O(M N)
        S: O(1)
        :param matrix:
        :return:
        """

        rows, cols = len(matrix), len(matrix[0])
        isCol = False

        for row in range(rows):
            if matrix[row][0] == 0:
                isCol = True
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if matrix[0][0] == 0:
            for col in range(cols):
                matrix[0][col] = 0

        if isCol:
            for row in range(rows):
                matrix[row][0] = 0

        return matrix


if __name__ == "__main__":
    matrices = Matrices()
    print(matrices.setMatrixToZero(
        [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    ))
    print(matrices.setMatrixToZero(
        [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    ))
