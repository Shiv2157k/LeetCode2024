from typing import List


class MaxConsecutiveOnesIII:

    def longest_ones(self, nums: List[int], k: int) -> int:
        """
        Approach: Sliding Window
        T: O(N)
        S: O(1)
        :param nums:
        :param k:
        :return:
        """
        right = 0
        left = 0

        while right < len(nums):

            k -= 1 - nums[right]

            if k < 0:
                k += 1 - nums[left]
                left += 1
            right += 1
        return right - left