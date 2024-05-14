from typing import List


class MissingNumber:

    def missing_number_v1(self, nums: List[int]) -> int:
        """
        Approach: Bit Manipulation XOR Operatoion
        t: O(N)
        S: O(1)
        :param nums:
        :return:
        """
        missing = len(nums)
        for i, num in enumerate(nums):
            missing = missing ^ i ^ num
        return missing

    def missing_number_v0(self, nums: List[int]) -> int:
        """
        Approach: MAth
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """
        n = len(nums)
        expected_sum = n * (n + 1) / 2
        curr_sum = 0
        for num in nums:
            curr_sum += num
        return expected_sum - curr_sum
