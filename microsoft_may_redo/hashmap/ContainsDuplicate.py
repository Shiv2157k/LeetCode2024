from typing import List


class ContainsDuplicate:

    def contains_duplicate(self, nums: List[int]) -> bool:
        """
        Approach: Freq HasMap
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """
        freq_map = {}
        for num in nums:
            freq_map = freq_map.get(num, 0) + 1
            if freq_map > 1:
                return True
        return False

    def containsDuplicate_v0(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False