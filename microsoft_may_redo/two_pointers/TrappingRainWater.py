from typing import List


class TrappingRainWater:

    def trap(self, height: List[int]) -> int:
        """
        Approach: Two Pointers
        T: O(N)
        S: O(1)
        :param height:
        :return:
        """
        left_max = 0
        right_max = 0
        max_area = 0

        left = 0
        right = len(height) - 1

        while left <= right:

            if height[left] <= height[right]:
                if left_max <= height[left]:
                    left_max = height[left]
                else:
                    max_area += left_max - height[left]
                left += 1
            else:
                if right_max <= height[right]:
                    right_max = height[right]
                else:
                    max_area += right_max - height[right]
                right -= 1
        return max_area
