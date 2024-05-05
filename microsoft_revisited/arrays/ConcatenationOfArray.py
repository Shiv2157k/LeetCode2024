from typing import List


class Array:

    def concatenation(self, nums: List[int]) -> List[int]:
        """
        Approach: Linear
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """
        n = len(nums)
        output: List[int] = [0] * (2 * n)

        for i in range(len(nums)):
            output[i] = nums[i]
            output[n + i] = nums[i]
        return output
