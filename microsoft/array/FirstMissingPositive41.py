from typing import List


class FirstMissingPositive:

    def firstMissingPositiveV1(self, nums: List[int]) -> int:
        """
        Approach: Cycle Sort
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """
        n = len(nums)
        index = 0

        while index < n:
            pos = nums[index] - 1
            if 0 < nums[index] <= n and nums[index] != nums[pos]:
                nums[pos], nums[index] = nums[index], nums[pos]
            else:
                index += 1

        for index in range(n):
            if nums[index] != index + 1:
                return index + 1
        return n + 1

    def firstMissingPositiveV0(self, nums: List[int]) -> int:
        """
        Approach: Index as a HashKey
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        # base case if there is no 1 in nums
        if 1 not in nums:
            return 1

        # Step 1: make all the numbers greater than num size and negative numbers to 1
        size = len(nums)
        for i, num in enumerate(nums):
            if num <= 0 or num > size:
                nums[i] = 1

        # Step 2: Hash to the index
        for i, num in enumerate(nums):

            value = abs(nums[i])

            if value == size:
                nums[0] = -abs(nums[0])
            else:
                nums[value] = -abs(nums[value])

        for i in range(1, size):
            if nums[i] > 0:
                return i

        if nums[0] > 0:
            return size

        return size + 1
