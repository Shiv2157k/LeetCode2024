from typing import List


class Matrix:

    def get_spiral_order(self, matrix: List[List[int]]) -> List[int]:
        """
        Approach: Delta Direction
        O(M * N)
        S: O(1)
        :param matrix:
        :return:
        """
        if not matrix:
            return []

        rows, cols = len(matrix), len(matrix[0])
        row = 0
        col = -1
        delta = 1
        spiral_order = []

        while rows * cols > 0:

            for _ in range(cols):
                col += delta
                spiral_order.append(matrix[row][col])
            rows -= 1

            for _ in range(rows):
                row += delta
                spiral_order.append(matrix[row][col])

            cols -= 1
            delta *= -1
        return spiral_order
