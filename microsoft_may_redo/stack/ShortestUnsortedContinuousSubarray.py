from typing import List


class ShortestUnsortedContinuousSubarray:

    def find_shortest_unsorted_subarray(self, nums: List[int]) -> int:
        """
        Approach: Stack to find left and right boundary
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        stack = []
        left = 0
        right = len(nums)

        for i in range(len(nums)):

            while stack and nums[stack[-1]] > nums[i]:
                left = min(left, stack.pop())

            stack.append(i)

        stack = []
        for i in range(len(nums) - 1, -1, -1):

            while stack and nums[stack[-1]] < nums[i]:
                right = max(right, stack.pop())
            stack.append(i)

        return 0 if right - left < 0 else right - left + 1
