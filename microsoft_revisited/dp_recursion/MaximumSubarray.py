from typing import List


class SubArray:

    def maximumSumV1(self, nums: List[int]) -> int:
        """
        Approach: DP
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        if len(nums) == 1:
            return nums[0]

        currSum = nums[0]
        maxSum = nums[0]

        for i in range(1, len(nums)):
            currSum = max(currSum, currSum + nums[i])
            maxSum = max(currSum, maxSum)
        return maxSum

    def maximumSumV0(self, nums: List[int]) -> int:
        """
        Approach: DP
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        if len(nums) == 1:
            return nums[0]

        dp = [float('inf')] * len(nums)
        dp[0] = nums[0]
        maxSum = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
            maxSum = max(maxSum, dp[i])
        return maxSum
