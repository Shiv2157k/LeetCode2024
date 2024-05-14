from typing import List


class MaximumProductSubArray:

    def max_product(self, nums: List[int]) -> int:
        """
        Approach: DP no extra space
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        if len(nums) == 0:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1, len(nums)):
            curr_max = max(max_so_far * nums[i], min_so_far * nums[i])
            curr_min = min(max_so_far * nums[i], min_so_far * nums[i])

            max_so_far = max(nums[i], curr_max)
            min_so_far = min(nums[i], curr_min)

            result = max(max_so_far, min_so_far)
        return result
