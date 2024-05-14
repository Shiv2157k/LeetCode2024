from typing import List


class HouseRobber:

    def rob_v0(self, nums: List[int]) -> int:
        """
        Approach: DP Tabulation
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for house in range(2, len(nums)):
            dp[house] += max(dp[house - 1], dp[house - 2] + nums[house])
        return dp[-1]

    def rob_v1(self, nums: List[int]) -> int:
        """
        Approach: Dp with no extra space
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        if len(nums) == 1:
            return nums[0]

        rob_curr = nums[0]
        rob_prev = 0

        for i in range(1, len(nums)):
            rob_next = max(rob_curr, rob_prev + nums[i])

            rob_prev = rob_curr
            rob_curr = rob_next
        return rob_curr
