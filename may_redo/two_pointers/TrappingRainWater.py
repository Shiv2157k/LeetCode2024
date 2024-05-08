from typing import List


class TrappingRainWater:

    def trap_v1(self, heights: List[int]) -> int:
        """
        Approach: Two Pointers
        T: O(N)
        S: O(1)
        :param height:
        :return:
        """
        if not heights:
            return 0

        length = len(heights)
        left_max = 0
        right_max = 0
        max_area = 0
        left = 0
        right = length - 1

        while left < right:

            if heights[left] <= heights[right]:
                if left_max <= heights[left]:
                    left_max = heights[left]
                else:
                    max_area += left_max - heights[left]
                left += 1
            else:
                if right_max <= heights[right]:
                    right_max = heights[right]
                else:
                    max_area += right_max - heights[right]
                right -= 1
        return max_area

    def trap_v0(self, heights: List[int]) -> int:
        """
        Approach: DP / Cummulative Sum
        T: O(N)
        S: O(N)
        :param heights:
        :return:
        """

        if not heights:
            return 0

        length = len(heights)
        left_max = [0] * length
        right_max = [0] * length

        left_max[0] = heights[0]
        for index in range(1, length):
            left_max[index] = max(heights[index], left_max[index - 1])

        right_max[-1] = heights[-1]
        for index in range(length - 2, -1, -1):
            right_max[index] = max(heights[index], right_max[index + 1])

        max_area = 0

        for index in range(1, length - 1):
            max_area += min(left_max[index], right_max[index]) - heights[index]
        return max_area
