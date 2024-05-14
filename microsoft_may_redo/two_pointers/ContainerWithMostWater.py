from typing import List


class ContainerWithMostWater:

    def max_area_with_water(self, heights: List[int]) -> int:
        """
        Approach: Two Pointers
        T: O(N)
        S: O(1)
        :param heights:
        :return:
        """

        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:

            breadth = right - left
            length = min(heights[left], heights[right])
            max_area = max(max_area, length * breadth)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return max_area
