from typing import List


class PascalTriangle:

    def generate(self, numRows: int) -> List[List[int]]:
        """
        Approach: Simulation
        T: O(NumRows^2)
        S: O(1)
        :param numRows:
        :return:
        """

        triangle = []

        for row_num in range(numRows):
            row = [0] * (row_num + 1)
            row[0] = 1
            row[-1] = 1

            for col in range(1, len(row) - 1):
                row[col] = triangle[row_num - 1][col - 1] + triangle[row_num - 1][col]
            triangle.append(row)
        return triangle
