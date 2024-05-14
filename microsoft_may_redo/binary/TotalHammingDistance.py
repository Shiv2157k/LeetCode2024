from typing import List


class TotalHammingDistance:

    def total_hamming_distance(self, nums: List[int]) -> int:
        """
        Approach: 32 bits count even and count odd
        T: O(32 * N)
        S: O(1)
        :param nums:
        :return:

        14 - 1110
        4 -  0100
        ---------
        hamming distance is 2
        """
        total_dist = 0
        for i in range(32):
            ones = 0

            for num in nums:
                ones += (num >> i) & 1
            total_dist += ones * (len(nums) - ones)
        return total_dist

    def total_hamming_distance_v0(self, nums: List[int]) -> int:

        max_num = max(nums)
        result = 0

        while max_num > 0:
            count_odd = 0
            count_even = 0

            for i in range(len(nums)):
                if nums[i] % 2 == 0:
                    count_even += 1
                else:
                    count_odd += 1
                nums[i] = nums[i] >> 1
            result += count_even * count_odd
            max_num = max_num >> 1
        return result
