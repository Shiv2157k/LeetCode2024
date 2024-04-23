from typing import List


class ContainerWithMostWater:

    def maxArea(self, height: List[int]) -> int:
        """
        Approach: Two Pointer / Greedy
        T: O(N)
        S: O(1)
        :param height:
        :return:
        """
        totalArea = 0

        left, right = 0, len(height) - 1

        while left < right:
            breadth = right - left
            length = min(height[left], height[right])
            totalArea = max(totalArea, length * breadth)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return totalArea
