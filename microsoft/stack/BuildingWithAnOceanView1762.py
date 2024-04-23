from typing import List


class OceanView:

    def getAllBuildings(self, heights: List[int]) -> List[int]:
        """
        Approach: Stack
        T: O(N)
        S: O(1) -> returning stack itself
        :param heights:
        :return:
        """

        stack = []
        for i in range(len(heights)):

            while stack and heights[stack[-1]] <= heights[i]:
                stack.pop()
            stack.append(i)
        return stack
