from typing import List


class PascalTriangle:

    def generate(self, numRows: int) -> List[List[int]]:
        """
        Approach: DP
        T: O(numRows^2)
        S: O(1)
        :param numRows:
        :return:
        """
        triangle = []

        for rowNum in range(numRows):

            row = [0] * (rowNum + 1)
            row[0], row[-1] = 1, 1

            for col in range(1, len(row) - 1):
                row[col] = triangle[rowNum - 1][col - 1] + triangle[rowNum - 1][col]

            triangle.append(row)
        return triangle
