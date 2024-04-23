from typing import List


class SpiralMatrix:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Approach: Pruning
        T: O(N * M)
        S: O(1)
        :param matrix:
        :return:
        """

        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, -1
        spiral = []
        direction = 1

        while rows * cols > 0:

            for _ in range(cols):
                col += direction
                spiral.append(matrix[row][col])
            rows -= 1

            for _ in range(rows):
                row += direction
                spiral.append(matrix[row][col])
            cols -= 1

            direction *= -1
        return spiral
