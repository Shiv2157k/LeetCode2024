from typing import List
from math import inf


class MaximumSubArray:

    def max_subarray(self, nums: List[int]) -> int:
        """
        Approach: DP without extra space
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        length = len(nums)
        if length == 1:
            return nums[0]

        curr_sum = nums[0]
        max_sum = nums[0]

        for index in range(1, length):
            curr_sum = max(nums[index] + curr_sum, nums[index])
            if curr_sum > max_sum:
                max_sum = curr_sum
        return max_sum

    def max_subarray_v0(self, nums: List[int]) -> int:
        """
        Approach: DP Tabulation
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        length = len(nums)
        if length == 1:
            return nums[0]

        dp = [-inf] * length
        dp[0] = nums[0]
        max_sum = nums[0]

        for index in range(1, length):
            dp[index] = max(dp[index - 1] + nums[index], nums[index])
            if max_sum < dp[index]:
                max_sum = dp[index]
        return max_sum
