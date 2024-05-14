from typing import List


class ClosestNumberToZero:

    def find(self, nums: List[int]) -> int:
        """
        Approach: Absolute diff
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        closest = nums[0]
        diff = abs(nums[0])

        for i in range(1, len(nums)):

            if abs(nums[i]) < diff:
                diff = abs(nums[i])
                closest = nums[i]

            if diff == abs(nums[i]) and nums[i] > closest:
                closest = nums[i]
        return closest
