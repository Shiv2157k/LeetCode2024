from typing import List


class PascalsTriangle:

    def generate(self, numRows: int) -> List[List[int]]:
        """
        Approach: DP
        T: O(NumRows * nmRows)
        S: O(0)
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
