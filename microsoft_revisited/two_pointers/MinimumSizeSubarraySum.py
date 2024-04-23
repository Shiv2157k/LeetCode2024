from typing import List
from math import inf


class MinimumSizeSubArraySum:

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Approach: Two Pointer
        T: O(N)
        S: O(1)
        :param target:
        :param nums:
        :return:
        """

        left, right = 0, 0
        totalSum = 0
        minSize = inf

        while right < len(nums):

            totalSum += nums[right]
            while totalSum >= target:
                minSize = min(minSize, right - left + 1)
                totalSum -= nums[left]
                left += 1
            right += 1
        return minSize if minSize != inf else 0
