from typing import List


class PartitionEqualSubSetSum:

    def can_partition_v2(self, nums: List[int]) -> bool:
        """
        Approach: Dp O(N)
        T: O(MN)
        S: O(N)
        :param nums:
        :return:
        """
        total = self.__calculate_total(nums)
        if total % 2 == 1:
            return False
        partition_sum = total // 2

        dp = [False] * (partition_sum + 1)
        dp[0] = True

        for curr in nums:
            for remain in range(partition_sum, curr - 1, -1):
                dp[remain] = dp[remain] or dp[remain - curr]
        return dp[partition_sum]

    def can_partition_v1(self, nums: List[int]) -> bool:
        """
        Approach: DP Tabulation
        T: O(NM)
        S: O(MN)
        :param nums:
        :return:
        """

        total = self.__calculate_total(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]
        # delimiter or sentinel
        dp[0][0] = True

        for ptr in range(1, len(nums) + 1):
            curr = nums[ptr - 1]
            for remain in range(target + 1):
                if remain < curr:
                    dp[ptr][remain] = dp[ptr - 1][remain]
                else:
                    dp[ptr][remain] = dp[ptr - 1][remain] or dp[ptr - 1][remain - curr]
        return dp[-1][-1]

    def __calculate_total(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            total += num
        return total

    def can_partition_v0(self, nums: List[int]) -> bool:
        """
        Approach: Recurse with memo
        T: O(m * n)
        S: O(m * n)
        :param nums:
        :return:
        """

        total = 0
        for num in nums:
            total += num

        if total % 2 == 1:
            return False

        def helper(ptr: int, remain: int):

            if remain == 0:
                return True
            if ptr == len(nums) or remain < 0:
                return False

            if memo[ptr][remain] != -1:
                return memo[ptr][remain] == 1

            is_partition = helper(ptr + 1, remain - nums[ptr]) or helper(ptr + 1, remain)
            memo[ptr][remain] = 1 if is_partition else 0
            return is_partition

        target = total // 2

        memo = [[-1] * (target + 1) for _ in range(len(nums) + 1)]
