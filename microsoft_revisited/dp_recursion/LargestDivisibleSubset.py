from typing import List


class Subset:

    def largest_divisible_subset(self, nums: List[int]) -> List[int]:
        """
        Approach: DP
        T: O(N log N + N^2 + N) -> O(N^2)
        S: O(N)
        :param nums:
        :return:
        """
        # step 1: sort the array that will reduce mod operation O(N^2) times twice
        nums.sort()

        # step 2: build dp and also find max len
        # initializing with 1 as every number is subset of itself
        dp: List[int] = [1] * (len(nums) + 1)
        # max_len for later subset retrieval should be minimum 1
        max_len: int = 1

        for right in range(1, len(nums)):
            for left in range(right):
                # if it is divisible and 1 + dp[left] is greater than right
                if nums[right] % nums[left] == 0 and 1 + dp[left] > dp[right]:
                    dp[right] = 1 + dp[left]
                    if max_len < dp[right]:
                        max_len = dp[right]

        # step 3: subset retrieval
        prev: int = -1
        subsets: List[int] = []

        for i in range(len(nums) - 1, -1, -1):

            if max_len == dp[i] and (prev == -1 or prev % nums[i] == 0):
                subsets.append(nums[i])
                max_len -= 1
                prev = nums[i]
        return subsets
