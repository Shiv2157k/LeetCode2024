from typing import List


class MaximalRectangle:

    def maximalRectangleV1(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix)

        # initialize left as the left most possible
        left = [0] * cols
        # initialize right as the right most possible
        right = [cols] * cols
        # calculating height of each row with this
        height = [0] * cols
        maxArea = 0

        for row in range(rows):

            currLeft, currRight = 0, cols

            for col in range(cols):

                if matrix[row][col] == '1':
                    height[col] += 1
                else:
                    height[col] = 0

            for col in range(cols):
                if matrix[row][col] == '1':
                    left[col] = max(left[col], currLeft)
                else:
                    left[col] = 0
                    currLeft = col + 1

            for col in range(cols - 1, -1, -1):
                if matrix[row][col] == '1':
                    right[col] = min(right[col], currRight)
                else:
                    right[col] = cols
                    currRight = col

            for col in range(cols):
                maxArea = max(maxArea, height[col] * (right[col] - left[col]))
        return maxArea

    def maximalRectangleV0(self, matrix: List[List[str]]) -> int:
        """
        Approach: DP + Stack
        T: O(MN)
        S: O(M)
        :param matrix:
        :return:
        """
        if not matrix:
            return 0

        maxArea = 0
        dp = [0] * len(matrix[0])

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):

                dp[col] = dp[col] + 1 if matrix[row][col] == '1' else 0

            maxArea = max(maxArea, self._getRectangleArea(dp))
        return maxArea

    def _getRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        maxArea = 0

        for i in range(len(heights)):

            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                currHeight = heights[stack.pop()]
                currWidth = i - stack[-1] - 1
                maxArea = max(maxArea, currWidth * currHeight)

            stack.append(i)

        while stack[-1] != -1:
            currHeight = heights[stack.pop()]
            currWidth = len(heights) - stack[-1] - 1
            maxArea = max(maxArea, currWidth * currHeight)
        return maxArea
