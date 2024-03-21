from typing import List


class RotatedSortedArray:

    def find_min(self, nums: List[int]) -> int:
        """
        Approach: Binary Search
        T: O( log N)
        S: O(1)
        :param nums:
        :return:
        """
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) - 1
        if nums[left] < nums[right]:
            return nums[left]

        while left <= right:

            pivot = left + (right - left) // 2

            # case1: pivot + 1 < pivot
            if nums[pivot + 1] < nums[pivot]:
                return nums[pivot + 1]
            # case2: pivot - 1 > pivot
            if nums[pivot - 1] > nums[pivot]:
                return nums[pivot]

            # if nums[pivot] is less than left
            # it should be on the right side
            if nums[pivot] > nums[0]:
                left = pivot + 1
            # otherwise left
            elif nums[pivot] < nums[0]:
                right = pivot - 1


if __name__ == "__main__":
    rotated_sorted_array = RotatedSortedArray()
    print(rotated_sorted_array.find_min([3, 4, 5, 1, 2]))
    print(rotated_sorted_array.find_min([3, 4, 5, 0, 1, 2]))
    print(rotated_sorted_array.find_min([3, 4, 5, 6, 7, 8]))
    print(rotated_sorted_array.find_min([9, 0, 1, 4, 7, 8]))