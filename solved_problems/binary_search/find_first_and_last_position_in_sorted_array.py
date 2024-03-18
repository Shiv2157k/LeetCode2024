from typing import List


class SortedArray:

    def first_and_last_post(self, nums: List[int], target: int) -> List[int]:
        """
        Approach: Binary Search
        T: O(log N)
        S: O(1)
        :param nums:
        :param target:
        :return:
        """
        left_bound = self.find_bound(nums, target, True)
        if left_bound == -1:
            return [-1, -1]
        right_bound = self.find_bound(nums, target, False)
        return [left_bound, right_bound]

    def find_bound(self, nums: List[int], target: int, is_left: bool) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:
            pivot = left + (right - left) // 2

            if nums[pivot] == target:
                if is_left:
                    if left == pivot or nums[pivot] != nums[pivot - 1]:
                        return pivot
                    else:
                        right = pivot - 1
                else:
                    if right == pivot or nums[pivot] != nums[pivot + 1]:
                        return pivot
                    else:
                        left = pivot + 1
            elif nums[pivot] < target:
                left = pivot + 1
            else:
                right = pivot - 1
        return -1


if __name__ == "__main__":
    sorted_array = SortedArray()
    print(sorted_array.first_and_last_post([1, 1, 2, 2, 7, 7, 9, 9], 9))
    print(sorted_array.first_and_last_post([1, 1, 2, 2, 7, 7, 9], 9))
    print(sorted_array.first_and_last_post([1, 1, 2, 2, 7, 7, 9, 9], 11))
    print(sorted_array.first_and_last_post([1, 1, 1, 2, 2, 7, 7, 9, 9], 1))
    print(sorted_array.first_and_last_post([1, 1, 2, 2, 7, 7, 7, 9, 9], 7))

