from typing import List


class Array:

    def minimize_maximum(self, nums: List[int]) -> int:
        """
        Approach: Greedy
        T: O(N)
        S: O(1)

        :param nums:
        :return:
        """

        max_value = 0
        cumm_sum = 0

        for index, num in enumerate(nums):
            cumm_sum += num
            if num > max_value:
                average_float = cumm_sum / (index + 1)
                average_int = int(-1 * average_float // 1 * -1)
                if average_int > max_value:
                    max_value = average_int
        return max_value
