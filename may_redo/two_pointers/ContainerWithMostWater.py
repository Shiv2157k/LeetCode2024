from typing import List


class ContainerWithMostWater:

    def max_area(self, height: List[int]) -> int:
        """
        Approach: Two Pointers
        T: O(N)
        S: O(1)
        :param height:
        :return:
        """

        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            breadth = right - left
            length = min(height[left], height[right])
            max_area = max(max_area, length * breadth)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area
