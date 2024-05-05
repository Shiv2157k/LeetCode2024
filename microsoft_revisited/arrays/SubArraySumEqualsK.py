from typing import List, Dict


class SubArray:

    def equals_k_v1(self, nums: List[int], k: int) -> int:
        """
        Approach: HashMap
        T: O(N)
        S: O(N)
        :param nums:
        :param k:
        :return:
        """

        sub_array_count: int = 0
        curr_sum: int = 0
        sum_occurrence_map: Dict[int, int] = {0: 1}

        for i in range(len(nums)):
            curr_sum += nums[i]
            if (curr_sum - k) in sum_occurrence_map:
                sub_array_count += sum_occurrence_map[curr_sum - k]
            sum_occurrence_map[curr_sum] = sum_occurrence_map.get(curr_sum, 0) + 1
        return sub_array_count

    def equals_k_v0(self, nums: List[int], k: int) -> int:
        """
        Approach: Brute Force
        T: O(N^2)
        S: O(N)
        :param nums:
        :param k:
        :return:
        """

        sub_array_sum: List[int] = [0] * (len(nums) + 1)
        total_sub_array: int = 0

        for i in range(1, len(nums)):
            sub_array_sum[i] = sub_array_sum[i - 1] + nums[i - 1]

        for left in range(len(nums)):
            for right in range(len(nums)):
                if sub_array_sum[right] - sub_array_sum[left] == k:
                    total_sub_array += 1
        return total_sub_array
