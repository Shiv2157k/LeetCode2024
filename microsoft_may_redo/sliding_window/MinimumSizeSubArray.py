from math import inf
from typing import List


class MinimumSizeSubArray:
    def min_sub_array_len(self, target: int, nums: List[int]) -> int:
        """
        Approach: Sliding Window
        T: O(N)
        S: O(1)
        :param target:
        :param nums:
        :return:
        """
        left, right = 0, 0
        total_sum = 0
        min_len = inf

        while right < len(nums):
            total_sum += nums[right]

            while total_sum >= target:
                min_len = min(min_len, right - left + 1)
                total_sum -= nums[left]
                left += 1
            right += 1
        return min_len if min_len != inf else 0
