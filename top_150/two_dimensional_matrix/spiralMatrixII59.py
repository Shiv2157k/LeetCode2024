from typing import List


class SpiralMatrixII:

    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        Approach: Traverse
        T: O(M * N)
        S: O(M * N)
        :param n:
        :return:
        """

        rows, cols = n, n
        row, col = 0, -1
        direction = 1

        spiralMatrix = [[0] * n for _ in range(n)]

        num = 1

        while num <= n * n:

            for _ in range(cols):
                col += direction
                spiralMatrix[row][col] = num
                num += 1
            rows -= 1

            for _ in range(rows):
                row += direction
                spiralMatrix[row][col] = num
                num += 1
            cols -= 1

            direction *= -1
        return spiralMatrix


if __name__ == "__main__":
    spiralMatrix = SpiralMatrixII()
    print(spiralMatrix.generateMatrix(3))
    print(spiralMatrix.generateMatrix(4))
