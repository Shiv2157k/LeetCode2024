from typing import List
from math import inf


class MaxSubArray:

    def get_maximum_sum(self, nums: List[int]) -> int:
        """
        Approach: DP
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """
        if len(nums) == 1:
            return nums[0]
        
        max_sum = nums[0]
        curr_sum = nums[0]

        for i in range(1, len(nums)):
            curr_sum = max(curr_sum + nums[i], nums[i])
            max_sum = max(max_sum, curr_sum)
        return max_sum
