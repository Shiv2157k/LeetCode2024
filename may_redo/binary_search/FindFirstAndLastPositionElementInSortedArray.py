from typing import List


class FirstAndLastPosition:

    def search_range(self, nums: List[int], target: int) -> List[int]:
        """
        Approach: Binary Search
        T: O(log N)
        S: O(1)
        :param nums:
        :param target:
        :return:
        """

        left_most = self._binary_search(nums, target, True)
        if left_most == -1:
            return [-1, -1]
        right_most = self._binary_search(nums, target, False)
        return [left_most, right_most]

    def _binary_search(self, nums: List[int], target: int, is_left: bool) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:

            pivot = left + (right - left) // 2

            if target == nums[pivot]:
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
            elif target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1
