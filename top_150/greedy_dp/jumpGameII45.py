from typing import List


class JumpGame:


    def minJumpNeededV1(self, nums: List[int]) -> int:
        """
        Approach: Greedy
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """
        currEnd, jumpSoFar = 0, 0
        minJump = 0

        for index in range(len(nums) - 1):

            if jumpSoFar < nums[index] + index:
                jumpSoFar = nums[index] + index

            if currEnd == index:
                minJump += 1
                currEnd = jumpSoFar
        return minJump

    def minJumpNeededV0(self, nums: List[int]) -> int:
        """
        Approach: DP
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        size = len(nums)
        if size == 1:
            return 0

        dp = [0] * size
        left = 0
        for index in range(size):
            while left + nums[left] < index:
                left += 1
            dp[index] = dp[left] + 1
        return dp[-1]


if __name__ == "__main__":
    jumpGame = JumpGame()
    print(jumpGame.minJumpNeededV1([2, 3, 1, 1, 4]))
    print(jumpGame.minJumpNeededV1([2, 3, 0, 1, 4]))

    print(jumpGame.minJumpNeededV0([2, 3, 1, 1, 4]))
    print(jumpGame.minJumpNeededV0([2, 3, 0, 1, 4]))