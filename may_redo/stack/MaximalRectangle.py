from typing import List


class MaximalRectangle:

    def maximal_rectangle(self, matrix: List[List[str]]):
        """
        Approach: DP + Stack
        T: O(MN)
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
                dp[col] = dp[col] + 1 if max_area[row][col] == '1' else 0
            max_area = max(max_area, self._get_rectangle_area(dp))
        return max_area

    def _get_rectangle_area(self, heights: List[List[int]]) -> int:
        stack = [-1]
        max_area = 0
        max_width = len(heights)

        for i in range(len(heights)):

            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                curr_height = heights[stack.pop()]
                curr_width = i - stack[-1] - 1
                max_area = max(max_area, curr_height * curr_width)
            stack.append(i)

        while stack[-1] != -1:
            curr_height = heights[stack.pop()]
            curr_width = max_width - stack[-1] - 1
            max_area = max(max_area, curr_height * curr_width)
        return max_area
