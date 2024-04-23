from typing import List


class ConcatenationArray:

    def getConcatenationArray(self, nums: List[int]) -> List[int]:
        """
        Approach: Linear
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """
        n = len(nums)
        output = [0] * (2 * n)

        for i in range(n):
            output[i] = nums[i]
            output[n + i] = nums[i]
        return output
