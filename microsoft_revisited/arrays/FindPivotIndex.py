from typing import List


class PivotIndex:

    def find(self, nums: List[int]) -> int:

        total_sum: int = 0
        for num in nums:
            total_sum += num

        left_sum: int = 0

        for i, num in enumerate(nums):
            if left_sum == (total_sum - left_sum - num):
                return i
            left_sum += num
        return -1
