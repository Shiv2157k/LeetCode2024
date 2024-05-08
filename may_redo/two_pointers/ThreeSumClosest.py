from typing import List
from math import inf


class ThreeSumClosest:

    def three_sum_closest(self, nums: List[int], target: int) -> int:
        """
        Approach: Two Pointers
        T: O(n^2)
        S: O(log n - n)
        :param nums:
        :param target:
        :return:
        """

        nums.sort()
        diff = inf

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                if abs(target - curr_sum) < abs(diff):
                    diff = target - curr_sum
                if curr_sum < target:
                    left += 1
                else:
                    right -= 1
            if diff == 0:
                break
        return target - diff
