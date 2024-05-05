from typing import List


class LargestRectangleInHistogram:

    def largest_rectangle_ares(self, heights: List[int]) -> int:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param heights:
        :return:
        """

        max_area = 0
        # delimiter
        stack = [-1]

        for i in range(len(heights)):
            # until we encounter non-increasing keep calculating the maxArea
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                length = heights[stack.pop()]
                breadth = i - stack[-1] - 1
                max_area = max(max_area, length * breadth)
            # stack will always have increasing sequence
            stack.append(i)

        # if there are still values in the stack
        while stack[-1] != -1:
            length = heights[stack.pop()]
            breadth = len(heights) - stack[-1] - 1
            max_area = max(max_area, length * breadth)
        return max_area
