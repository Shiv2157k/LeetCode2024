from typing import List


class SortedArray:

    def search(self, nums: List[int], target: int):
        """
        Approach: Binary Search
        T: O( log N)
        S: O(1)
        :param nums:
        :param target:
        :return:
        """

        left: int = 0
        right: int = len(nums) - 1

        while left <= right:
            pivot = left + (right - left) // 2

            if nums[pivot] > target:
                right = pivot - 1
            elif nums[pivot] < target:
                left = pivot + 1
            else:
                return pivot
        return -1
