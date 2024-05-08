from typing import List


class TwoSum:

    def two_sum(self, nums: List[int], target: int):
        """
        Approach: Hash Map
        T: O(N)
        S: O(N)
        :param nums:
        :param target:
        :return:
        """

        complement_map = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in complement_map:
                return [complement_map[complement], i]
            complement_map[num] = i
        return [-1, -1]
