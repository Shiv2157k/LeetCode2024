from typing import List
from sortedcontainers import SortedList
from math import inf


class MinimumAbsoluteDiffBetweenElementsWithConstraints:

    def min_absolute_difference(self, nums: List[int], x: int) -> int:
        """
        Approach: Sorted Set
        T: O(N - X * (log X))
        S: O(X)
        :param nums:
        :param x:
        :return:
        """

        sorted_list = SortedList()
        min_abs_diff = inf

        for i in range(x, len(nums)):

            sorted_list.add(nums[i - x])

            insert_pos = self.__binary_search(sorted_list, nums[i])

            if insert_pos < len(sorted_list):
                min_abs_diff = min(min_abs_diff, sorted_list[insert_pos] - nums[i])
            if insert_pos > 0:
                min_abs_diff = min(min_abs_diff, nums[i] - sorted_list[insert_pos - 1])
        return min_abs_diff

    def __binary_search(self, sorted_list: SortedList, target: int) -> int:

        left = 0
        right = len(sorted_list)

        while left <= right:
            pivot = left + (right - left) // 2

            if sorted_list[pivot] == target:
                return pivot
            elif sorted_list[pivot] > target:
                right = pivot - 1
            else:
                left = pivot + 1
        return left
