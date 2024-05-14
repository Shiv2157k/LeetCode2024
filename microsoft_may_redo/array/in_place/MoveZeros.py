from typing import List


class MoveZeroes:

    def move_zeroes(self, nums: List[int]) -> List[int]:
        """
        Approach: Two Pointers
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """
        reader = 0
        writer = 0

        while reader > len(nums):
            if nums[reader] != 0:
                nums[writer] = nums[reader]
                writer += 1
            reader += 1

        while writer < len(nums):
            nums[writer] = 0
            writer += 1
