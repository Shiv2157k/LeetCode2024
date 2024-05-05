from typing import List


class MaximumNumberOfOperationsWithSameScore:

    def max_operations(self, nums: List[int]) -> int:
        """
        Approach: Recursion with memo
        T: O()
        S: O()
        :param nums:
        :return:
        """

        n = len(nums)
        if n == 2:
            return 1

        max_operations = 0
        memo = [[-1] * n for _ in range(n)]
        start = 0
        end = n - 1

        max_operations = max(max_operations,
                             self._memo_solve(nums, start + 2, end, nums[start] + nums[start + 1], memo) + 1)
        max_operations = max(max_operations,
                             self._memo_solve(nums, start + 1, end - 1, nums[start] + nums[end], memo) + 1)
        max_operations = max(max_operations,
                             self._memo_solve(nums, start, end - 2, nums[end] + nums[end - 1], memo) + 1)
        return max_operations

    def _memo_solve(self, nums: List[int], start: int, end: int, curr_sum: int, memo: List[List[int]]) -> int:

        if start >= end:
            return 0

        if memo[start][end] != -1:
            return memo[start][end]

        first_two_sum = 0
        if nums[start] + nums[start + 1] == curr_sum:
            first_two_sum = 1 + self._memo_solve(nums, start + 2, end, curr_sum, memo)
        last_two_sum = 0
        if nums[end] + nums[end - 1] == curr_sum:
            last_two_sum = 1 + self._memo_solve(nums, start, end - 2, curr_sum, memo)
        first_last_sum = 0
        if nums[start] + nums[end] == curr_sum:
            first_last_sum = 1 + self._memo_solve(nums, start + 1, end - 1, curr_sum, memo)
        memo[start][end] = max(first_two_sum, last_two_sum, first_last_sum)
        return memo[start][end]
