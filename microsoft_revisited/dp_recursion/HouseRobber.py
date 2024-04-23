from typing import List


class HouseRobber:

    def robV1(self, nums: List[int]) -> int:
        """
        Approach: DP
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for index in range(2, len(nums)):
            dp[index] = max(dp[index - 2] + nums[index], dp[index - 1])
        return dp[-1]

    def robV0(self, nums: List[int]) -> int:
        """
        Approach: DP
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """
        memo = {}

        def helper(house):

            if house == 0:
                return nums[house]
            if house == 1:
                return max(nums[house], nums[house - 1])
            if house in memo:
                return memo[house]

            memo[house] = max(helper(house - 1), helper(house - 2) + nums[house])
            return memo[house]

        return helper(len(nums) - 1)
