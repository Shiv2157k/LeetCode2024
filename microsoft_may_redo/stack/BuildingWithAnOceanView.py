from typing import List


class Buildings:

    def get_ocean_view_building_positions(self, heights: List[int]) -> List[int]:
        """
        Approach: STack
        T: O(N)
        S: O(1)
        :param heights:
        :return:
        """

        stack = []

        for i in range(len(heights)):

            while stack and heights[stack[-1]] <= heights[i]:
                stack.pop()
            stack.append(i)
        return stack
