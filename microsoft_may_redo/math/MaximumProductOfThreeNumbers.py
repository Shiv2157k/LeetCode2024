from typing import List
from math import inf


class MaximumProductOfThreeNumbers:

    def max_product(self, nums: List[int]) -> int:
        """
        Approach: Min and Max
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """
        if len(nums) == 3:
            return nums[0] + nums[1] + nums[2]

        max1 = -inf
        max2 = -inf
        max3 = -inf

        min1 = inf
        min2 = inf

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

        product = max(max1 * max2 * max3, max1 * min1 * min2)

        return product
