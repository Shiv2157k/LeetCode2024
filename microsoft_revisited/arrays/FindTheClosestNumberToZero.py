from typing import List


class ClosestNumber:

    def find_to_zero(self, nums: List[int]) -> int:
        """
        Approach: Diff
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """
        
        output: int = nums[0]
        diff: int = abs(nums[0])

        for i in range(1, len(nums)):

            if abs(nums[i]) < diff:
                diff = abs(nums[i])
                output = nums[i]

            if diff == abs(nums[i]) and nums[i] > output:
                output = nums[i]
        return output
