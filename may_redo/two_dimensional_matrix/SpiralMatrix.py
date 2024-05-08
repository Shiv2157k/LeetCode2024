from typing import List


class SpiralMatrix:


    def generate_order(self, matrix: List[List[int]]) -> List[int]:
        """
        Approach: Simulation
        T: O(M * N)
        S: O(1)
        :param matrix:
        :return:
        """

        rows = len(matrix)
        cols = len(matrix[0])
        row, col = 0, -1
        direction = 1
        order = []

        while rows * cols > 0:

            for _ in range(cols):
                col += direction
                order.append(matrix[row][col])
            rows -= 1

            for _ in range(rows):
                row += direction
                order.append(matrix[row][col])
            cols -= 1

            direction *= -1
        return order