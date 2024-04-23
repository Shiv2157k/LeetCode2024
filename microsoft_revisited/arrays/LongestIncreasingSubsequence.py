from typing import List


class LongestIncreasingSubsequence:

    def longest_increasing_subseq_v2(self, nums: List[int]) -> int:
        """
        Approach: Binary Search
        T: O(N * log N)
        S: O(N)
        :param nums:
        :return:
        """

        sub_seq = [nums[0]]

        for i in range(1, len(nums)):

            if nums[i] > sub_seq[-1]:
                sub_seq.append(nums[i])
            else:
                ptr = self._binary_search(sub_seq, nums[i])
                sub_seq[ptr] = nums[i]
        return len(nums)

    def _binary_search(self, sub: List[int], target: int) -> int:
        left: int = 0
        right: int = len(sub)

        while left < right:
            pivot = left + (right - left) // 2
            if target == sub[pivot]:
                return pivot
            elif target > sub[pivot]:
                left = pivot + 1
            else:
                right = pivot
        return left

    def longest_increasing_subseq_v1(self, nums: List[int]) -> int:
        """
        Approach: Intelligently build a sequence
        T: O(N) -> Worst Case O(N^2)
        S: O(N)
        :param nums:
        :return:
        """

        sub_seq = [nums[0]]

        for i in range(1, len(nums)):

            if nums[i] > sub_seq[-1]:
                sub_seq.append(nums[i])
            else:
                ptr = 0
                while nums[i] > sub_seq[ptr]:
                    ptr += 1
                sub_seq[ptr] = nums[i]
        return len(sub_seq)

    def longest_increasing_subseq_v0(self, nums: List[int]) -> int:
        """
        Approach: DP
        T: O(N ^2)
        S: O(N)
        :param nums:
        :return:
        """

        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):

                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])

        maxSeq: int = 0
        for seq in dp:
            maxSeq = max(maxSeq, seq)
        return maxSeq
