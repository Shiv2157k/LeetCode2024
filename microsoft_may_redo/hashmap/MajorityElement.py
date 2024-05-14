from typing import List


class MajorityElement:

    def majority_element(self, nums: List[int]) -> int:
        """
        Approach: HashMap
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        freq_map = {}
        max_freq = 0
        candidate = nums[0]

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

            if max_freq < freq_map[num]:
                max_freq = freq_map[num]
                candidate = num
        return candidate
