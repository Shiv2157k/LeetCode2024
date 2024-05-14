from typing import List


class RemoveElement:

    def remove_element(self, nums: List[int], val: int) -> List[int]:
        """
        Approach: Two Pointers
        T: O(N)
        S: O(1)
        :param nums:
        :param val:
        :return:
        """

        writer = 0

        for reader in range(len(nums)):
            if nums[reader] != val:
                nums[writer] = nums[reader]
                writer += 1
            reader += 1
        return writer