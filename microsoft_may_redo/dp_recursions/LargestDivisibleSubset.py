from typing import List


class LargestDivisibleSubset:

    def get_largest(self, nums: List[int]) -> List[int]:
        """
        Approach: DP Tabulation
        T: O(N log N + N^2 + N) -> O(N^2)
        S: O(N)
        :param nums:
        :return:
        """

        # to decrease mod operation and time complexity good to sort
        nums.sort()

        # every number is subset of itself
        dp = [1] * len(nums)
        max_len = 1

        for right in range(1, len(nums)):
            for left in range(right):

                if nums[right] % nums[left] == 0 and 1 + dp[left] > dp[right]:
                    dp[right] = 1 + dp[left]
                    if max_len < dp[right]:
                        max_len = dp[right]

        prev = -1
        subsets = []

        for i in range(len(nums) - 1, -1, -1):

            if max_len == dp[i] and (prev == -1 or prev % nums[i] == 0):
                subsets.append(nums[i])
                max_len -= 1
                prev = nums[i]
        return subsets
