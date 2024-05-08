from sortedcontainers import SortedList
from bisect import bisect_left
from typing import List
from math import inf


class DivideArrayWithMinCostII:

    def get_min_cost(self, nums: List[int], k: int, dist: int) -> int:
        """
        Approach: Sliding Window + SortedList
        T: O(n * (log K + k))
        S: O(K + dist)
        :param nums:
        :param k:
        :param dist:
        :return:
        """

        num_length = len(nums)

        # Initialize a sorted list to maintain a sorted order of numbers
        sorted_list = SortedList()

        # The first element in the nums list as the starting point
        starting_num = nums[0]

        # Initialize the answer to infinite for future comparison
        min_cost = float("inf")

        # The window starts from the first element
        left_index = 1

        # Running sum of the k-1 elements
        running_sum = 0

        # Loop through the nums list starting from the second element
        for right_index in range(1, num_length):
            # Find the position where nums[right_index] should be inserted
            insert_pos = bisect_left(sorted_list, nums[right_index])

            # Add the current number to the sorted list
            sorted_list.add(nums[right_index])

            # If the insert position is less than k - 1, update the running sum
            if insert_pos < k - 1:
                running_sum += nums[right_index]
                # If the sorted list has more than k - 1 elements, subtract the k-th element
                if len(sorted_list) > k - 1:
                    running_sum -= sorted_list[k - 1]

            # If the window size is larger than allowed by 'dist', adjust the window from the left
            while right_index - left_index > dist:
                # Find the index of the left-most number to be removed
                removed_index = sorted_list.index(nums[left_index])
                # Remove the left-most element
                removed_num = nums[left_index]
                sorted_list.remove(removed_num)

                # Adjust the running sum based on the position of the removed element
                if removed_index < k - 1:
                    running_sum -= removed_num
                    # If there are still at least k - 1 elements, add the (k-1)-th element to the running sum
                    if len(sorted_list) >= k - 1:
                        running_sum += sorted_list[k - 2]
                # Move the left window index to the right
                left_index += 1

            # If the window size is at least k - 1, calculate the cost to consider this subarray
            if right_index - left_index + 1 >= k - 1:
                min_cost = min(min_cost, running_sum)

        # Return the minimum cost added with the first element that was set aside
        return min_cost + starting_num
