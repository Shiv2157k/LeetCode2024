from typing import List


class FindClosestNumberToZero:

    def findClosestToZero(self, nums: List[int]) -> int:
        """
        Approach: Linear with abs fun
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        ans = nums[0]
        diff = abs(nums[0])

        for i in range(1, len(nums)):

            if abs(nums[i]) < diff:
                diff = abs(nums[i])
                ans = nums[i]

            if abs(nums[i]) == diff and nums[i] > ans:
                ans = nums[i]
        return ans
