from typing import List
from enum import Enum, auto


class Index(Enum):
    GOOD = auto()
    BAD = auto()
    UNKNOWN = auto()


class JumpGame:

    def canJumpFromPosV1(self, nums: List[int]) -> bool:
        """
        Approach: Greedy
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        maxJump = 0

        for index in range(len(nums)):
            if maxJump < nums[index] + index:
                maxJump = nums[index] + index
            if maxJump == index:
                break
        return maxJump >= len(nums) - 1

    def canJumpFromPosV0(self, nums: List[int]) -> bool:
        """
        Approach: DP
        T: O(MN)
        S: O(N)
        :param nums:
        :return:
        """

        length = len(nums)

        dp = [Index.UNKNOWN] * length
        dp[-1] = Index.GOOD

        for index in range(length - 2, -1, -1):
            jump = min(index + nums[index], length - 1)
            for nextIndex in range(index + 1, jump + 1):
                if dp[nextIndex] == Index.GOOD:
                    dp[index] = Index.GOOD
                    break
        return dp[0] == Index.GOOD


if __name__ == "__main__":
    
    jumpGame = JumpGame()
    print(jumpGame.canJumpFromPosV0([2, 3, 1, 1, 4]))
    print(jumpGame.canJumpFromPosV1([2, 3, 1, 1, 4]))

    print(jumpGame.canJumpFromPosV0([3, 2, 1, 0, 4]))
    print(jumpGame.canJumpFromPosV1([3, 2, 1, 0, 4]))
