from typing import List


class MaxNumberOfOperation:

    def maxOperations(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 2:
            return 1

        result = 0
        memo = [[-1] * n for _ in range(n)]

        left, right = 0, n - 1

        result = max(result, self.helper(nums, left + 2, right, nums[left] + nums[left + 1], memo) + 1)
        result = max(result, self.helper(nums, left + 1, right - 1, nums[left] + nums[right], memo) + 1)
        result = max(result, self.helper(nums, left, right - 2, nums[right - 1] + nums[right], memo) + 1)

        return result

    def helper(self, nums: List[int], left: int, right: int, currSum: int, memo: List[List[int]]):

        if left >= right:
            return 0

        if memo[left][right] != -1:
            return memo[left][right]

        firstTwo = 0

        if nums[left] + nums[left + 1] == currSum:
            firstTwo = 1 + self.helper(nums, left + 2, right, currSum, memo)

        firstAndLast = 0
        if nums[left] + nums[right] == currSum:
            firstAndLast = 1 + self.helper(nums, left + 1, right - 1, currSum, memo)

        lastTwo = 0
        if nums[right - 1] + nums[right] == currSum:
            lastTwo = 1 + self.helper(nums, left, right - 2, currSum, memo)

        memo[left][right] = max(firstTwo, firstAndLast, lastTwo)

        return memo[left][right]


if __name__ == "__main__":
    maxNumberOfOperation = MaxNumberOfOperation()
    print(maxNumberOfOperation.maxOperations([3, 2, 1, 2, 3, 4]))
