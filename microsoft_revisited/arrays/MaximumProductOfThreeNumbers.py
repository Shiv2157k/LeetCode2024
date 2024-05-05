from typing import List
from math import inf


class MaximumProduct:

    def of_three_numbers(self, nums: List[int]) -> int:
        """
        Approach: Min and Max
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]

        max1: float = -inf
        max2: float = max1
        max3: float = max2

        min1: float = inf
        min2: float = min1

        for num in nums:

            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num

            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
        return max(min1 * min2 * max1, max1 * max2 * max3)
