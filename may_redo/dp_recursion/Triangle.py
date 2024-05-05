from typing import List
from math import inf
class Triangle:


    def minimum_total_v1(self, triangle: List[List[int]]) -> int:
        """
        Approach: DP LastRow
        T: O(N * M)
        S: O(N)
        :param triangle:
        :return:
        """
        last_row = triangle[-1]
        rows = len(triangle)

        for row in range(rows - 2, -1, -1):
            curr_row = []
            for col in range(row + 1):
                min_sum = min(last_row[col], last_row[col + 1])
                curr_row.append(triangle[row][col] + min_sum)
            last_row = curr_row
        return last_row[0]

    def minimum_total_v0(self, triangle: List[List[int]]) -> int:
        """
        Approach: DP Top Down
        :param triangle:
        :return:
        """

        rows = len(triangle)

        for row in range(1, rows):
            for col in range(row + 1):
                min_sum = inf
                if col > 0:
                    min_sum = triangle[row - 1][col - 1]
                elif col < row:
                    min_sum = min(min_sum, triangle[row - 1][col])
                triangle[row][col] += min_sum
        return min(triangle[-1])