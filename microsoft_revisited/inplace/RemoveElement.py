from typing import List


class UnSortedArray:

    def removeElementV1(self, nums: List[int], val: int):
        """
        Approach: Reader and writer
        T: O(N)
        S: O(1)
        :param nums:
        :param val:
        :return:
        """
        writer = 0
        for reader, num in enumerate(nums):

            if num != val:
                nums[writer] = num
                writer += 1
        return writer

    def removeElementV0(self, nums: List[int], val: int):
        """
        Approach: Two Pointers when elements to remove are rare
        T: O(N)
        S: O(1)
        :param nums:
        :param val:
        :return:
        """
        ptr = 0
        n = len(nums)

        while ptr < n:

            if nums[ptr] == val:
                nums[ptr] = nums[n - 1]
                n -= 1
            else:
                ptr += 1
        return n
