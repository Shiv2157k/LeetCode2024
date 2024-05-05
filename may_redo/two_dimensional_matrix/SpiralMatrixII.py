from typing import List


class SpiralMatrixII:

    def generate_spiral_matrix(self, n: int) -> List[List[int]]:
        """
        Approach: Offset
        T: O(M * N)
        S: O(1)
        :param n:
        :return:
        """

        spiral_matrix = [[0] * n for _ in range(n)]
        direction = 1
        row = 0
        col = -1
        rows, cols = n, n

        num = 1

        while num <= n * n:

            for _ in range(cols):
                col += direction
                spiral_matrix[row][col] = num
                num += 1
            rows -= 1

            for _ in range(rows):
                row += direction
                spiral_matrix[row][col] = num
                num += 1
            cols -= 1
            direction *= -1
        return spiral_matrix
