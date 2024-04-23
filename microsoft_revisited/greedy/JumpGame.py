from typing import List
from enum import Enum, auto


class Index(Enum):
    GOOD = auto()
    BAD = auto()
    UNKNOWN = auto()


class JumpGame:

    def canJumpV1(self, nums: List[int]) -> bool:
        """
        Approach: Greedy
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        maxReach, length = 0, len(nums)

        for index in range(length):

            if maxReach < nums[index] + index:
                maxReach = nums[index] + index
            if maxReach == index:  # cannot jump further
                break
        return maxReach >= length - 1

    def canJumpV0(self, nums: List[int]) -> bool:

        length = len(nums)
        dp = [Index.UNKNOWN] * length
        dp[-1] = Index.GOOD

        for index in range(length - 2, -1, -1):
            jump = min(nums[index] + index, length - 1)
            for nextIndex in range(index + 1, jump + 1):
                if dp[index] == Index.GOOD:
                    dp[index] = Index.GOOD
                    break
        return dp[0] == Index.GOOD
