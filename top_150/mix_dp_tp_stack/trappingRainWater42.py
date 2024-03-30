from typing import List


class RainWater:

    def trapAreaV1(self, height: List[int]) -> int:
        """
        Approach: Two Pointer
        T: O(N)
        S: O(1)
        :param height:
        :return:
        """
        if not height:
            return 0
        size = len(height)

        left, right = 0, size - 1
        leftMax, rightMax = 0, 0
        maxArea = 0

        while left <= right:

            if height[left] < height[right]:
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    maxArea += leftMax - height[left]
                left += 1
            else:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    maxArea += rightMax - height[right]
                right -= 1
        return maxArea

    def trapAreaV0(self, height: List[int]) -> int:
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
        maxArea = 0
        leftMax = [0] * size
        rightMax = [0] * size

        leftMax[0] = height[0]

        for index in range(1, size):
            leftMax[index] = max(height[index], leftMax[index - 1])

        rightMax[-1] = height[-1]

        for index in range(size - 2, -1, -1):
            rightMax[index] = max(height[index], rightMax[index + 1])

        for index in range(1, size - 1):
            maxArea += min(leftMax[index], rightMax[index]) - height[index]

        return maxArea


if __name__ == "__main__":
    rainWater = RainWater()
    print(rainWater.trapAreaV0([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(rainWater.trapAreaV1([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

    print(rainWater.trapAreaV0([4, 2, 0, 3, 2, 5]))
    print(rainWater.trapAreaV1([4, 2, 0, 3, 2, 5]))
