from typing import List


class Positive:

    def firstMissingV1(self, nums: List[int]) -> int:
        """
        Approach: Cycle Sort
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        if 1 not in nums:
            return 1

        size = len(nums)
        index = 0

        while index < len(nums):
            pointer = nums[index] - 1

            if 0 < nums[index] <= size and nums[index] != nums[pointer]:
                nums[index], nums[pointer] = nums[pointer], nums[index]
            else:
                index += 1

        for i in range(size):
            if nums[i] != i + 1:
                return i + 1
        return size + 1

    def firstMissingV0(self, nums: List[int]) -> int:
        """
        Approach: Index Hash
        T: O(N)
        S: O(1)

        :param nums:
        :return:
        """

        # base
        if 1 not in nums:
            return 1

        size = len(nums)

        # hash out < 1 and > len(nums) with 1
        for i in range(size):

            if nums[i] <= 0 or nums[i] > size:
                nums[i] = 1

        # has index with negative
        for i in range(size):

            val = abs(nums[i])

            if val == size:
                nums[0] = -abs(nums[0])
            else:
                nums[val] = -abs(nums[val])

        for i in range(1, size):
            if nums[i] > 0:
                return i

        if nums[0] > 0:
            return size
        return size + 1
