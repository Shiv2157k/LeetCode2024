from typing import List


class MaximumProduct:

    def ofThreeNumbers(self, nums: List[int]) -> int:
        """
        Approach: Single Scan
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]

        # max1, max2, max3 = -1000, -1000, -1000
        # min1, min2 = 1000, 1000
        max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')
        min1, min2 = float('inf'), float('inf')

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
