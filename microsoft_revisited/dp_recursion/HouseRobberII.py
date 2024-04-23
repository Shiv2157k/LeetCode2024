from typing import List


class HouseRobberII:

    def rob(self, nums: List[int]) -> int:

        # base cases
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        return max(self._rob_house(nums, 0, len(nums) - 1), self._rob_house(nums, 1, len(nums)))

    def _rob_house(self, nums: List[int], start: int, end: int):

        dp = [0] * (end - start)

        dp[0] = nums[start]
        dp[1] = max(nums[start + 1], dp[0])

        for house in range(start + 2, end):
            dp[house - start] = max(nums[house] + dp[house - start - 2], dp[house - start - 1])
        return dp[-1]
