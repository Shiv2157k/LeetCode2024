from typing import List


class PeakElement:


    def findV0(self, nums: List[int]) -> int:
        """
        Approach: Linear
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1

    def findV1(self, nums: List[int]) -> int:
        """
        Approach: Binary Search
        T: O(log N)
        S: O(1)
        :param nums:
        :return:
        """

        left, right = 0, len(nums) - 1
        while left < right:
            pivot = left + (right - left) // 2
            if nums[pivot] > nums[pivot + 1]:
                right = pivot
            if nums[pivot] < nums[pivot + 1]:
                left = pivot + 1
        return left

