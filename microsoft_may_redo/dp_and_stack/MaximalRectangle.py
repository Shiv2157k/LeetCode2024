from typing import List


class MaximalRectangle:

    def maximal_rectangle(self, matrix: List[List[int]]) -> int:
        """
        Approach: DP and stack
        T: O(NM)
        S: O(M)
        :param matrix:
        :return:
        """
        if len(matrix) == 0:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        max_area = 0

        dp = [0] * cols

        for row in range(rows):
            for col in range(cols):
                dp[col] = dp[col] + 1 if matrix[row][col] == '1' else 0
            max_area = max(max_area, self._calculate_area(dp))
        return max_area

    def _calculate_area(self, heights: List[int]) -> int:
        """
        Approach: Stack
        :param heights:
        :return:
        """

        stack = [-1]
        max_area = 0

        for i in range(len(heights)):

            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                curr_height = heights[stack.pop()]
                curr_width = i - stack[-1] - 1
                max_area = max(max_area, curr_height * curr_width)
            stack.append(i)

        while stack[-1] != -1:
            curr_height = heights[stack.pop()]
            curr_width = len(heights) - stack[-1]
            max_area = max(max_area, curr_height * curr_width)
        return max_area
