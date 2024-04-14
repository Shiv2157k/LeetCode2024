from typing import List


class Histogram:

    def largestRectangle(self, heights: List[int]) -> int:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param heights:
        :return:
        """

        stack = [-1]

        maxArea = 0

        for i in range(len(heights)):
            while stack != [-1] and heights[stack[-1]] >= heights[i]:
                currHeight = heights[stack.pop()]
                currWidth = i - stack[-1] - 1
                maxArea = max(maxArea, currHeight * currWidth)
            stack.append(i)

        while stack[-1] != -1:
            currHeight = heights[stack.pop()]
            currWidth = len(heights) - stack[-1] - 1
            maxArea = max(maxArea, currHeight * currWidth)
        return maxArea
