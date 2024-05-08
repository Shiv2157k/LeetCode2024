from typing import List


class SortedArray:

    def remove_duplicates(self, nums: List[int]) -> int:
        """
        Approach:
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """
        writer = 1
        for reader in range(1, len(nums)):
            if nums[reader] != nums[reader - 1]:
                nums[writer] = nums[reader]
                writer += 1
        return writer
