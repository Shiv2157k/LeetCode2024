from typing import List


class SpiralMatrix:

    def getOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Approach: Single Pass
        T: O(M * N)
        S: O(M * N)
        :param matrix:
        :return:
        """

        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, -1
        result = []
        direction = 1

        while rows * cols > 0:

            for _ in range(cols):
                col += direction
                result.append(matrix[row][col])
            rows -= 1

            for _ in range(rows):
                row += direction
                result.append(matrix[row][col])
            cols -= 1

            direction *= -1
        return result


if __name__ == "__main__":
    spiralMatrix = SpiralMatrix()
    print(spiralMatrix.getOrder(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ))
    print(spiralMatrix.getOrder(
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

    ))
