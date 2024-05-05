from typing import List


class OceanView:

    def get_buildings(self, heights: List[int]):
        """
        Approach:
        :param heights:
        :return:
        """

        stack: List[int] = []

        for i in range(len(heights)):

            while stack and heights[stack[-1]] <= heights[i]:
                stack.pop()
            stack.append(i)
        return stack
