from typing import List


class SingleNumber:

    def single_number_v1(self, nums: List[int]) -> int:

        single = 0

        for num in nums:
            single = single ^ num
        return single

    def single_number_v0(self, nums: List[int]) -> int:
        num_freq = {}
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1

        for num, freq in num_freq.items():
            if freq == 1:
                return num
        return -1
