from typing import List


class PeakElement:

    def find(self, nums: List[int]) -> int:
        """
        Approach: Binary Search with Pruning
        T: O(log N)
        S: O(1)
        :param nums:
        :return:
        """

        left = 0
        right = len(nums) - 1

        while left < right:
            pivot = left + (right - left) // 2

            if nums[pivot] > nums[pivot + 1]:
                right = pivot
            if nums[pivot] < nums[pivot + 1]:
                left = pivot + 1
        return left
