from typing import List


class MaximumSizeSubArraySumEqualsK:

    def max_sub_array_len(self, nums: List[int], k: int) -> int:
        """
        Approach: Hash Map + Prefix Sum
        :param nums:
        :param k:
        :return:
        """

        running_sum = 0
        longest = 0
        sum_indices_map = {}

        for i, num in enumerate(nums):

            running_sum += num
            # Check if all of the numbers seen so far sum to k.
            if running_sum == k:
                longest = i + 1
            # If any subarray seen so far sums to k, then
            # update the length of the longest_subarray.
            if running_sum - k in sum_indices_map:
                longest = max(longest, i - sum_indices_map[running_sum - k])
            # Only add the current prefix_sum index pair to the
            # map if the prefix_sum is not already in the map.
            if running_sum not in sum_indices_map:
                sum_indices_map[running_sum] = i
        return longest
