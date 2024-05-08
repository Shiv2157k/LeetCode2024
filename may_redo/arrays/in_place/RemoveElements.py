from  typing import List


class Array:

    def remove_elements(self, nums: List[int], val: int) -> int:
        """
        Approach: Reader and writer
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
        return writer