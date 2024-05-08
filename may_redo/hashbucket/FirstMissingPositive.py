from typing import List


class FirstMissingPositive:

    def first_missing_positive_v1(self, nums: List[int]) -> int:
        """
        Approach: Cycle Sort
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        size = len(nums)
        ptr = 0

        while ptr < size:
            ideal_ptr = nums[ptr] - 1

            if 0 < nums[ptr] <= size and nums[ptr] != nums[ideal_ptr]:
                nums[ptr], nums[ideal_ptr] = nums[ideal_ptr], nums[ptr]
            else:
                ptr += 1

        for i in range(size):
            if nums[i] != i + 1:
                return i + 1
        return size + 1

    def first_missing_positive_v0(self, nums: List[int]) -> int:
        """
        Approach: index as hash
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        if 1 not in nums:
            return 1

        size = len(nums)

        # Step1:
        # - flip all numbers less than or equal to 0 -> 1
        # - flip all numbers greater than size -> 1
        for i in range(size):
            if nums[i] <= 0 or nums[i] > size:
                nums[i] = 1

        # Step 2: Index as hash with negative numbers
        for i in range(size):
            val = abs(nums[i])

            # special case if val == size
            if val == size:
                nums[0] = -abs(nums[0])
            else:
                nums[val] = -abs(nums[val])

        # Step 3: Traverse through 1 - size - 1
        # first non-negative index is our answer
        for i in range(1, size):
            if nums[i] > 0:
                return i
        if nums[0] > 0:  # reached here then it can be size
            return size
        # reached here it is size + 1
        return size + 1
