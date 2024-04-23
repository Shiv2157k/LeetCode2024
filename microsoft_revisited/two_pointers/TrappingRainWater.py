from typing import List


class RainWater:

    def trapV1(self, height: List[int]) -> int:
        """
        Approach: Two Pointers
        T: O(N)
        S: O(N)
        :param height:
        :return:
        """

        if not height:
            return 0

        size = len(height)
        left, right = 0, size - 1

        leftMax, rightMax = 0, size - 1
        maxArea = 0

        while left < right:

            if height[left] < height[right]:
                if leftMax <= height[left]:
                    leftMax = height[left]
                else:
                    maxArea += leftMax - height[left]
                left += 1
            else:
                if rightMax <= height[right]:
                    rightMax = height[right]
                else:
                    maxArea += rightMax - height[right]
                right -= 1
        return maxArea

    def trapV0(self, height: List[int]) -> int:
        """
        Approach: DP
        T: O(N)
        S: O(N)
        :param height:
        :return:
        """
        if not height:
            return 0
        size = len(height)
        leftMax = [0] * size
        rightMax = [0] * size

        leftMax[0] = height[0]

        for index in range(1, size):

            leftMax[index] = max(height[index], leftMax[index - 1])

        rightMax[-1] = height[-1]

        for index in range(size - 2, -1, -1):
            rightMax[index] = max(height[index], rightMax[index + 1])

        maxArea = 0

        for index in range(1, size - 1):
            maxArea += min(leftMax[index], rightMax[index]) - height[index]
        return maxArea
