from typing import List


class LargestRectangleInHistogram:

    def largest_rectangle_area(self, heights: List[int]) -> int:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param heights:
        :return:
        """
        # sentinel or delimiter for left boundary
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
            curr_width = len(heights) - stack[-1] - 1
            max_area = max(max_area, curr_height * curr_width)
        return max_area
