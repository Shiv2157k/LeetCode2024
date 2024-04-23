from typing import List


class RotatedSortedArray:

    def findMinimum(self, nums: List[int]) -> int:
        """
        Approach: Binary Search
        T: O(log N)
        S: O(1)
        :param nums:
        :return:
        """

        left, right = 0, len(nums) - 1

        while left <= right:
            pivot = left + (right - left) // 2

            if nums[pivot - 1] > nums[pivot]:
                return nums[pivot]
            elif nums[pivot] > nums[pivot + 1]:
                return nums[pivot + 1]

            if nums[pivot] > nums[0]:
                left = pivot + 1
            elif nums[pivot] < nums[0]:
                right = pivot - 1
