from typing import List
from pprint import pprint


class PascalTriangle:

    def generate(self, numRows: int) -> list[list[int]]:
        """
        Approach: DP
        T: O(numRows^2)
        S: O(1)
        :param numRows:
        :return:
        """

        triangle = []

        for rowNum in range(numRows):
            row = [0 for _ in range(rowNum + 1)]
            row[0], row[rowNum] = 1, 1
            for col in range(1, len(row) - 1):
                row[col] = triangle[rowNum - 1][col - 1] + triangle[rowNum - 1][col]
            triangle.append(row[:])
        return triangle


if __name__ == "__main__":
    pascalTriangle = PascalTriangle()
    pprint(pascalTriangle.generate(5))
