from typing import List


class PartitionEqualSubsetSum:

    def can_partition_v2(self, nums: List[int]) -> bool:
        """
        Approach: DP Space Optimized
        T: O(m * n)
        S: O(m)
        :param nums:
        :return:
        """

        total: int = 0
        for num in nums:
            total += num

        if total % 2 != 0:
            return False

        partition_sum: int = total // 2

        dp: List[bool] = [False] * (partition_sum + 1)
        dp[0] = True

        for curr in nums:
            for remain in (partition_sum, curr - 1, -1):
                dp[remain] = dp[remain] or dp[remain - curr]
        return dp[partition_sum]

    def can_partition_v1(self, nums: List[int]) -> bool:
        """
        Approach: DP Bottom Up
        T: O(m * n)
        S: O(m * n)
        :param nums:
        :return:
        """

        total: int = 0
        for num in nums:
            total += num

        if total % 2 == 1:
            return False

        target: int = total // 2

        dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = True

        for ptr in range(1, len(nums) + 1):
            curr = nums[ptr - 1]
            for remain in range(target + 1):
                if remain < curr:
                    dp[ptr][remain] = dp[ptr - 1][remain]
                else:
                    dp[ptr][remain] = dp[ptr - 1][remain] or dp[ptr - 1][remain - curr]
        return dp[len(nums)][target]

    def can_partition_v0(self, nums: List[int]) -> bool:
        """
        Approach: Recurse with memo
        T: O(m * n)
        S: O(m * n)
        :param nums:
        :return:
        """

        # step 1: calculate the total sum
        total: int = 0
        for num in nums:
            total += num

        # step 2: validation check
        if total % 2 != 0:
            return False

        # step 3: partition value calculation
        target: int = total // 2

        # step 4: build the memo dp
        memo: List[List[int]] = [[-1] * (target + 1) for _ in range(len(nums) + 1)]

        # step 5: call the recurse with memo helper
        return self._helper(nums, 0, target, memo)

    def _helper(self, nums: List[int], ptr: int, target: int, memo: List[List[int]]) -> bool:
        """
        Recurse with memo helper function
        :param nums:
        :param ptr:
        :param target:
        :param memo:
        :return:
        """

        # base cases
        if target == 0:
            return True
        if target < 0 or ptr == len(nums):
            return False
        # if we already went through the process
        # i.e., if it's in our memo stack
        if memo[ptr][target] != -1:
            return memo[ptr][target] == 1

        # apply the recurse for two cases
        # case 1: we subtract curr number from target
        # case 2: we skip to the next number without subtract
        is_partition: bool = self._helper(nums, ptr + 1, target - nums[ptr], memo) or self._helper(nums, ptr + 1,
                                                                                                   target, memo)

        # store the is_partition value to our memo dp
        memo[ptr][target] = 1 if is_partition else 0
        return is_partition
