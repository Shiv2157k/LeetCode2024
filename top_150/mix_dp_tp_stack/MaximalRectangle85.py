from typing import List


class Rectangle:

    def getMaxAreaV1(self, matrix: List[List[str]]) -> int:
        """
        Approach: Stack Histogram
        T: O(MN)
        S: O(N)
        :param matrix:
        :return:
        """

        maxArea = 0
        rows, cols = len(matrix), len(matrix[0])

        dp = [0] * cols

        for row in range(rows):
            for col in range(cols):
                dp[col] = dp[col] + 1 if matrix[row][col] == "1" else 0

            maxArea = max(maxArea, self._calculateHistogramArea(dp))
        return maxArea

    def _calculateHistogramArea(self, height: List[int]) -> int:

        stack = [-1]
        maxArea = 0

        for i, presentHeight in enumerate(height):

            while stack[-1] != -1 and height[stack[-1]] >= presentHeight:
                currHeight = height[stack.pop()]
                currWidth = i - stack[-1] - 1
                maxArea = max(maxArea, currWidth * currHeight)

            stack.append(i)

        while stack[-1] != -1:
            currHeight = height[stack.pop()]
            currWidth = len(height) - stack[-1] - 1
            maxArea = max(maxArea, currWidth * currHeight)
        return maxArea

    def getMaxAreaV0(self, matrix: List[List[str]]) -> int:
        """
        Approach: DP expand from middle
        T: O(MN)
        S: O(N)
        :param matrix:
        :return:
        """

        rows, cols = len(matrix), len(matrix[0])
        # left most col
        left = [0] * cols
        # right most col
        right = [cols] * cols
        # to capture height
        height = [0] * cols
        maxArea = 0

        for row in range(rows):

            currLeft, currRight = 0, cols

            # height
            for col in range(cols):
                if matrix[row][col] == '1':
                    height[col] = 1
                else:
                    height[col] = 0

            # left
            for col in range(cols):
                if matrix[row][col] == '1':
                    currLeft = max(left[col], currLeft)
                else:
                    currLeft = col + 1
                    left[col] = 0

            # right
            for col in range(cols - 1, -1, -1):
                if matrix[row][col] == '1':
                    currRight = min(right[col], currRight)
                else:
                    currRight = col
                    right[col] = cols

            # update max Area
            for col in range(cols):
                maxArea = max(maxArea, height[col] * (right[col] - left[col]))

        return maxArea
