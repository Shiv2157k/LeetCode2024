from typing import List


class FindPivotIndex:

    def pivot_index(self, nums: List[int]) -> int:
        """
        Approach: Prefix Sum
        T: O(log N)
        S: O(1)
        :param nums:
        :return:
        """

        prefix_sum = 0
        for num in nums:
            prefix_sum += num

        left_sum = 0
        for i, num in enumerate(nums):
            if left_sum == prefix_sum - left_sum - num:
                return i
            left_sum += num
        return -1
