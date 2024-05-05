from typing import List


class SingleNumberII:

    def single_number_ii_v1(self, nums: List[int]) -> int:
        """
        Approach: Bit Manipulation
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        seen_once = 0
        seen_twice = 0

        for num in nums:
            seen_once = (seen_once ^ num) & (~seen_twice)
            seen_twice = (seen_twice ^ num) & (~seen_once)
        return seen_once

    def single_number_v0(self, nums: List[int]) -> int:
        num_freq = {}
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1

        for num, freq in num_freq.items():
            if freq == 1:
                return num
        return -1
