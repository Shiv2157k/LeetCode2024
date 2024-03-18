from typing import List


class RotatedSortedArray:

    def find_target(self, nums: List[int], target: int) -> int:
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
            # case 1: if we have found the target
            if target == nums[pivot]:
                return pivot
            # case 2: if left side is sorted
            elif nums[left] <= nums[pivot]:
                if nums[left] <= target < nums[pivot]:
                    right = pivot - 1
                else:
                    left = pivot + 1
            else:  # case 3: if right side is sorted
                if nums[right] >= target > nums[pivot]:
                    left = pivot + 1
                else:
                    right = pivot - 1
        # if we came here there is no target in the array
        return -1


if __name__ == "__main__":
    rotated_sorted_array = RotatedSortedArray()
    print(rotated_sorted_array.find_target([5, 6, 7, 0, 3, 4], 4))
    print(rotated_sorted_array.find_target([5, 6, 7, 0, 3, 4], 0))
    print(rotated_sorted_array.find_target([5, 6, 7, 0, 3, 4], 5))
    print(rotated_sorted_array.find_target([5, 6, 7, 0, 3, 4], 6))
    print(rotated_sorted_array.find_target([5, 6, 7, 0, 3, 4], 7))
    print(rotated_sorted_array.find_target([0], 0))
    print(rotated_sorted_array.find_target([1, 2], 2))
    print(rotated_sorted_array.find_target([], 2))
    print(rotated_sorted_array.find_target([1], 3))
