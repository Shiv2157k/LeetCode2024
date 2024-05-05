from typing import List
from sortedcontainers import SortedSet
from math import inf


class Array:

    def min_absolute_difference(self, nums: List[int], x: int):
        """
        Approach: SortedSet
        T: O()
        S: O()
        :param nums:
        :param x:
        :return:
        """

        sorted_set = SortedSet()
        min_abs_diff = inf

        for i in range(x, len(nums)):
            sorted_set.add(nums[i - x])
            # Find the index in the sorted list where nums[i] would fit
            insert_pos = sorted_set.bisect_left(sorted_set, nums[i])
            # If there is an element on the right, update min_diff
            if insert_pos < len(sorted_set):
                min_abs_diff = min(min_abs_diff, sorted_set[insert_pos] - nums[i])
            # If there is an element on the left, update min_diff
            if insert_pos > 0:
                min_abs_diff = min(min_abs_diff, nums[i] - sorted_set[insert_pos - 1])
        return min_abs_diff
