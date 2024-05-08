from typing import List


class SearchInsertPosition:

    def search_insert(self, nums: List[int], target: int) -> int:
        """
        Approach: Binary Search
        T: O(log N)
        S: O(1)
        :param nums:
        :param target:
        :return:
        """

        left = 0
        right = len(nums) - 1

        while left <= right:
            pivot = left + (right - left) // 2

            if target == nums[pivot]:
                return pivot
            elif target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return left
