from typing import List


class MaximumProductSubArray:

    def maxProduct(self, nums: List[int]) -> int:
        """
        Approach: DP
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """
        if len(nums) == 0:
            return 0

        maxSoFar = nums[0]
        minSoFar = nums[0]
        result = maxSoFar

        for i in range(1, len(nums)):

            currMax = max(minSoFar * nums[i], maxSoFar * nums[i])
            currMin = min(minSoFar * nums[i], maxSoFar * nums[i])

            maxSoFar = max(nums[i], currMax)
            minSoFar = min(nums[i], currMin)

            result = max(maxSoFar, result)
        return result