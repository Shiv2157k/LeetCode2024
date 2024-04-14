from typing import List


class SpiralMatrix:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        rows = len(matrix)
        cols = len(matrix[0])
        row, col = 0, -1

        direction = 1
        spiral = []

        while rows * cols:

            for _ in range(cols):
                cols += direction
                spiral.append(matrix[row][col])
            rows -= 1

            for _ in range(rows):
                rows += direction
                spiral.append(matrix[row][col])
            cols -= 1

            direction *= -1
        return spiral
