from typing import List


class ClosestNumberToZero:

    def find(self, nums: List[int]) -> int:
        """
        Approach: Linear
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        output = nums[0]
        diff = abs(nums[0])

        for i in range(1, len(nums)):

            if abs(nums[i]) < diff:
                output = nums[i]
                diff = abs(nums[i])

            if diff == abs(nums[i]) and nums[i] > output:
                output = nums[i]

        return output
