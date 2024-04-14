from typing import List


class RotatedSortedArrayII:

    def search(self, nums: List[int], target: int) -> bool:
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
                return True
            elif nums[left] == nums[pivot] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[pivot]:  # left is non rotated
                if nums[left] <= target < nums[pivot]:
                    right = pivot - 1
                else:
                    left = pivot + 1
            elif nums[right] >= nums[pivot]:  # right is non rotated
                if nums[right] >= target > nums[pivot]:
                    left = pivot + 1
                else:
                    right = pivot - 1
        return False


if __name__ == "__main__":
    rotatedSortedArr = RotatedSortedArrayII()
    print(rotatedSortedArr.search([2, 5, 6, 0, 0, 1, 2], 0))
    print(rotatedSortedArr.search([2, 5, 6, 0, 0, 1, 2], 7))
