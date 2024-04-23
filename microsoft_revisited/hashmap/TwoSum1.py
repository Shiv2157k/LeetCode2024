from typing import List


class TwoSum:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Approach: One Pass Hash Table
        T: O(N)
        S: O(N)
        :param nums:
        :param target:
        :return:
        """

        complementMap = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in complementMap and complementMap[complement] != i:
                return [complement[complementMap], i]
            complementMap[num] = i
        return [-1, -1]
