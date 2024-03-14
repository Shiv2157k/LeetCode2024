from typing import List


class RainWater:

    def trap_v2(self, height: List[int]) -> int:
        """
        Approach: Two Pointers
        T: O(N)
        S: O(1)
        :param height:
        :return:
        """
        max_area = 0
        left, right = 0, len(height) - 1
        left_max = right_max = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    max_area += left_max - height[left]
                left += 1
            else: # height[left] >= height[right
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    max_area += right_max - height[right]
                right -= 1
        return max_area

    def trap_v1(self, height: List[int]) -> int:
        """
        Approach: DP
        T: O(N)
        S: O(N)
        :param height:
        :return:
        """
        max_area = 0
        size = len(height)
        left_max = [0] * size
        right_max = [0] * size
        left_max[0] = height[0]
        for i in range(1, size):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[-1] = height[-1]
        for i in range(size - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        for i in range(size):
            max_area += min(left_max[i], right_max[i]) - height[i]
        return max_area

    def trap_v0(self, height: List[int]) -> int:
        """
        BRute Force
        :param heights:
        :return:
        """
        size = len(height)
        max_area = 0

        for i in range(1, len(size)):
            left_max = right_max = 0

            for j in range(i, -1, -1):
                left_max = max(left_max, height[j])

            for j in range(i, size - 1):
                right_max = max(right_max, height[j])

            max_area += min(left_max, right_max) - height[i]
        return max_area