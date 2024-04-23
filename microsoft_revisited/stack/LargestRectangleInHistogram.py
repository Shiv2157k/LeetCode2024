from typing import List


class Histogram:

    def largestRectangleArea(self, heights: List[int]) -> int:
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

            # until we encounter non-increasing keep calculating
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                currHeight = heights[stack.pop()]
                currWidth = i - stack[-1] - 1
                maxArea = max(maxArea, currHeight * currWidth)
            # push to stack when it is increasing order i.e., 1, 2, 3
            stack.append(i)

        while stack[-1] != -1:
            currHeight = heights[stack.pop()]
            currWidth = len(heights) - stack[-1] - 1
            maxArea = max(maxArea, currHeight * currWidth)
        return maxArea
