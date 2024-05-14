from sortedcontainers import SortedList
from bisect import bisect_left
from math import inf
from typing import List


class DivideAnArrayIntoSubArraysWithMinimumCost:

    def minimum_cost(self, nums: List[int], k: int, dist: int) -> int:
        """
        Approach: Sliding Window with SortedList
        T: O(n * (log K + k))
        S: O(K + dist)
        :param nums:
        :param k:
        :return:
        """

        sorted_list = SortedList()
        min_cost = 0
        running_sum = 0
        length = len(nums)
        left = 1
        start_num = nums[0]

        for right in range(1, length):

            # get the insert position
            insert_pos = bisect_left(sorted_list, nums[right])

            # add it to the sorted list
            sorted_list.append(nums[right])

            if insert_pos < k - 1:
                # add it into the running sum
                running_sum += nums[right]
                if len(sorted_list) > k - 1:
                    # update the running sum decrementing with the last index val
                    running_sum -= sorted_list[k - 1]

            # check if this is a valid window and shrink accordingly
            while right - left > dist:
                pos_to_remove = sorted_list.index(nums[left])
                val_to_remove = nums[left]
                sorted_list.remove(val_to_remove)

                if pos_to_remove < k - 1:
                    running_sum -= val_to_remove
                    if len(sorted_list) >= k - 1:
                        running_sum += sorted_list[k - 2]

                left += 1

            if right - left + 1 >= k - 1:
                min_cost = min(min_cost, running_sum)
        return min_cost + start_num
