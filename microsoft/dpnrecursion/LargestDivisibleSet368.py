from typing import List



class LargestDivisibleSubSet:


    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        # validation
        if len(nums) == 0:
            return 1

        # min max len is 1
        maxLen = 1
        # Step 1: Sort the array
        nums.sort()

        # Step 2: initialize and build the dp
        dp = [1] * (len(nums) + 1)

        for right in range(1, len(nums)):
            for left in range(right):

                if nums[right] % nums[left] == 0 and 1 + dp[left] > dp[right]:
                    dp[right] = 1 + dp[left]
                    if dp[right] > maxLen:
                        maxLen = dp[right]

        # Step 3: Build the subsets
        prev = -1
        subsets = []
        for i in range(len(nums) - 1, -1, -1):
            if maxLen == dp[i] and (prev == -1 or prev % nums[i] == 0):
                subsets.append(nums[i])
                maxLen -= 1
                prev = nums[i]
        return subsets
