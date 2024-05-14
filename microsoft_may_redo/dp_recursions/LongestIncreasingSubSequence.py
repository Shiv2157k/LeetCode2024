from typing import List


class LongestIncreasingSubSequence:

    def length_of_lis_v1(self, nums: List[int]) -> int:
        """
        Approach: Intelligently build a sequence with BS
        T: O(N log N)
        S: O(N)
        :param nums:
        :return:
        """

        sub = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] > sub[-1]:
                sub.append(nums[i])
            else:
                ptr = self.__binary_search(sub, nums[i])
                sub[ptr] = nums[i]
        return len(sub)

    def __binary_search(self, sub: List[int], target: int):
        left = 0
        right = len(sub) - 1

        while left < right:
            pivot = left + (right - left) // 2
            if target == sub[pivot]:
                return pivot
            elif target > sub[pivot]:
                left = pivot + 1
            else:
                right = pivot - 1
        return left

    def length_of_lis_v1(self, nums: List[int]) -> int:
        """
        Approach: Intelligently build a sequence
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        sub = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] > sub[-1]:
                sub.append(nums[i])
            else:
                ptr = 0
                while nums[i] > sub[ptr]:
                    ptr += 1
                sub[ptr] = nums[i]
        return len(sub)

    def length_of_lis_v0(self, nums: List[int]) -> int:
        """
        Approach: DP with Tabulation
        T: O(N^2)
        S: O(N)
        :param nums:
        :return:
        """
        dp = [1] * len(nums)

        for p1 in range(1, len(nums)):
            for p2 in range(p1):
                if nums[p1] > nums[p2]:
                    dp[p1] = max(dp[p2] + 1, dp[p1])
        return max(dp)
