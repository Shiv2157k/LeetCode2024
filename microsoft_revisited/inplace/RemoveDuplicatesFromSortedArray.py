from typing import List


class SortedArray:

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Approach: Two Indexes Approach
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """
        insertPtr = 1

        for i in range(1, len(nums)):

            if nums[i] != nums[i - 1]:
                nums[insertPtr] = nums[i]
                insertPtr += 1
        return insertPtr
