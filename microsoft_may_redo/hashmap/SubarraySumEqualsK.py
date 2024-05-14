from typing import List


class Arrays:

    def subarray_sum_equals_k(self, nums: List[int], k: int) -> int:
        """
        Approach: HashMap
        T: O(N)
        S: O(N)
        :param nums:
        :param k:
        :return:
        """

        total = 0
        curr_sum = 0
        sum_occurrence_map = {0: 1}
        for num in nums:
            curr_sum += num
            if curr_sum - k in sum_occurrence_map:
                total += sum_occurrence_map[curr_sum - k]
            sum_occurrence_map[curr_sum] = sum_occurrence_map.get(curr_sum, 0) + 1
        return total