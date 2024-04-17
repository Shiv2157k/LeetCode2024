from typing import List


class ShortestUnSortedContinuousSubArray:

    def findUnSortedSubArrayLenV1(self, nums: List[int]) -> int:
        """
        Approach: Without extra space
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """
        right = -1
        maxSeen = float('-inf')

        for i in range(len(nums)):
            maxSeen = max(maxSeen, nums[i])
            if nums[i] < maxSeen:
                right = i

        left = 0
        minSeen = float('inf')
        for i in range(len(nums) - 1, -1, -1):
            minSeen = min(minSeen, nums[i])
            if nums[i] > minSeen:
                left = i
        return right - left + 1

    def findUnSortedSubArrayLenV0(self, nums: List[int]) -> int:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        stack = []

        left, right = len(nums), -1

        for i in range(len(nums)):

            while stack and nums[stack[-1]] > nums[i]:
                left = min(left, stack.pop())
            stack.append(i)

        stack = []

        for i in range(len(nums) - 1, -1, -1):

            while stack and nums[stack[-1]] < nums[i]:
                right = max(right, stack.pop())
            stack.append(i)
        return right - left + 1
