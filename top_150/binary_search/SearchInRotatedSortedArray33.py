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
            elif nums[left] <= nums[pivot]:  # assume left subarray is sorted
                # if target is with in this range move right to left
                if nums[left] <= target < nums[pivot]:
                    right = pivot - 1
                else:
                    left = pivot + 1
            else:  # assume right sub array is sorted
                if nums[pivot] < target <= nums[right]:
                    left = pivot + 1
                else:
                    right = pivot - 1
        return -1


if __name__ == "__main__":
    arr = RotatedSortedArray()
    print(arr.search([4, 5, 6, 7, 0, 1, 2], 0))
    print(arr.search([4, 5, 6, 7, 0, 1, 2], 3))
    print(arr.search([1], 1))
    print(arr.search([0], 1))
