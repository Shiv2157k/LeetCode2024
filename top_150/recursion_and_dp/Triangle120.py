from typing import List
from math import inf


class Triangle:

    def minTotalSumV1(self, triangle: List[List[int]]) -> int:
        """
        Approach: DP Auxiliary Space
        T: O(N^2)
        S: O(N)
        :param triangle:
        :return:
        """

        lastRow = triangle[-1]

        rows = len(triangle)

        for row in range(rows - 2, -1, -1):
            currRow = []
            for col in range(row + 1):
                minSum = min(lastRow[col], lastRow[col + 1])
                currRow.append(triangle[row][col] + minSum)
            lastRow = currRow
        return lastRow[0]

    def minTotalSumV0(self, triangle: List[List[int]]) -> int:
        """
        Approach: DP inplace
        T: O(M * N)
        S: O(1)
        :param triangle:
        :return:
        """

        rows = len(triangle)

        for row in range(1, rows):
            for col in range(row + 1):
                minSum = inf
                if col > 0:
                    minSum = triangle[row - 1][col - 1]
                if col < row:
                    minSum = min(minSum, triangle[row - 1][col])
                triangle[row][col] += minSum
        return min(triangle[-1])


if __name__ == "__main__":

    triangles = Triangle()
    print(triangles.minTotalSumV0(
        [[6], [2, 8], [4, 2, 3], [9, 5, 7, 2]]
    ))
    print(triangles.minTotalSumV1(
        [[6], [2, 8], [4, 2, 3], [9, 5, 7, 2]]
    ))