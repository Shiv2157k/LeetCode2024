from typing import List


class RotatedSortedArray:

    def search(self, nums: List[int], target: int) -> int:
        """
        Approach: Binary Search
        T: O(log N)
        S: O(1)
        :param nums:
        :param target:
        :return:
        """

        left, right = 0, len(nums) - 1

        while left <= right:
            pivot = left + (right - left) // 2

            if nums[pivot] == target:
                return pivot
            elif nums[left] <= nums[pivot]:
                if nums[left] <= target < nums[pivot]:
                    right = pivot - 1
                else:
                    left = pivot + 1
            else:
                if nums[right] >= target > nums[pivot]:
                    left = pivot + 1
                else:
                    right = pivot - 1
        return -1
