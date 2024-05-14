from typing import List


class SameScoreII:

    def max_number_of_operations_with_same_score(self, nums: List[int]) -> int:
        """
        Approach: Recursion with memo
        T: O(N^2)
        S: O(N^2) -> max depth of recursion is O(N)
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

        max_operations = max(max_operations, self.helper(nums, start + 2, end, nums[start] + nums[start + 1], memo) + 1)
        max_operations = max(max_operations, self.helper(nums, start - 1, end - 1, nums[start] + nums[end], memo) + 1)
        max_operations = max(max_operations, self.helper(nums, start, end - 2, nums[end - 1] + nums[end], memo) + 1)

        return max_operations

    def helper(self, nums: List[int], start, end, curr_sum, memo):

        # base case
        if start >= end:
            return 0

        if memo[start][end] != -1:
            return memo[start][end]

        first_two_sum = 0

        if nums[start] + nums[start + 1] == curr_sum:
            first_two_sum = 1 + self.helper(nums, start + 2, end, curr_sum, memo)

        first_last_sum = 0
        if nums[start] + nums[end] == curr_sum:
            first_last_sum = 1 + self.helper(nums, start + 1, end - 1, curr_sum, memo)

        last_two_sum = 0
        if nums[end] + nums[end - 1] == curr_sum:
            last_two_sum = 1 + self.helper(nums, start, end - 2, curr_sum, memo)

        memo[start][end] = max(first_two_sum, first_last_sum, last_two_sum)
        return memo[start][end]
