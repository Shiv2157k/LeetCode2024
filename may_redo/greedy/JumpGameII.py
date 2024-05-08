from typing import List


class JumpGameII:

    def minimum_jumps_v1(self, nums: List[int]) -> int:
        """
        Approach: Greedy
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        n = len(nums)
        curr_end = 0
        curr_far = 0
        min_jumps = 0

        for i in range(n - 1):

            if curr_far < nums[i] + i:
                curr_far = nums[i] + i

            if i == curr_end:
                min_jumps += 1
                curr_end = curr_far
        return min_jumps

    def minimum_jumps_v0(self, nums: List[int]) -> int:
        """
        Approach: DP
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        n = len(nums)
        if n == 1:
            return 0
        dp = [0] * n
        j = 0

        for i in range(1, n):
            while j + nums[j] < i:
                j += 1
            dp[i] = dp[j] + 1
        return dp[-1]
