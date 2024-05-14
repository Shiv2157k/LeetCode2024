from typing import List


class HouseRobberII:

    def rob(self, nums: List[int]) -> int:
        """
        Approach: DP with memo
        T: O(N * N)
        S: O(N)
        :param nums:
        :return:
        """

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        start_from_house1 = self.__rob_house(nums, 0, len(nums) - 1)
        start_from_house2 = self.__rob_house(nums, 1, len(nums))
        return max(start_from_house1, start_from_house2)

    def __rob_house(self, nums: List[int], start_house: int, end_house: int) -> int:
        """
        DP
        :param nums:
        :param start_house:
        :param end_house:
        :return:
        """

        dp = [0] * (end_house - start_house)
        dp[0] = nums[start_house]
        dp[1] = max(nums[start_house], nums[end_house])

        for house in range(start_house + 2, end_house):
            dp[house - start_house] = max(dp[house - start_house - 2] + nums[house], dp[house - start_house - 1])
        return dp[-1]

    def __rob_house_v1(self, nums: List[int], start_house: int, end_house: int) -> int:
        t1 = 0
        t2 = 0
        for house in range(start_house, end_house):
            t1, t2 = max(nums[house] + t2, t1), t1
            """
            temp = t1
            t1 = max(nums[house] + t2, t1)
            t2 = temp
            """
        return t1

