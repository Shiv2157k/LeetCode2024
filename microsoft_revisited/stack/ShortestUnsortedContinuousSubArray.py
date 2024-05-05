from typing import List
from math import inf


class UnsortedContinuousSubArray:

    def find_unsorted_continuous_sub_arr_v0(self, nums: List[int]) -> int:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        stack: List[int] = []
        left: int = len(nums)

        for i in range(len(nums)):

            while stack and nums[i] < nums[stack[-1]]:
                left = min(left, stack.pop())
            stack.append(i)

        stack: List[int] = []
        right: int = 0

        for i in range(len(nums), -1, -1):

            while stack and nums[i] > nums[stack[-1]]:
                right = max(right, stack.pop())
            stack.append(i)
        return 0 if right - left < 0 else right - left + 1