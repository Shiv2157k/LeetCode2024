from typing import List


class FirstMissingPositive:


    def first_missing_positive(self, nums: List[int]) -> int:
        """
        Approach: Cycle Sort
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """
        if 1 not in nums:
            return 1

        size = len(nums)
        ptr = 0

        while ptr < size:

            ideal_ptr = nums[ptr] - 1

            if 0 < nums[ideal_ptr] <= size and nums[ptr] != nums[ideal_ptr]:
                nums[ptr], nums[ideal_ptr] = nums[ideal_ptr], nums[ptr]
            else:
                ptr += 1

        for i in range(size):
            if nums[ptr] != i + 1:
                return i + 1
        return size + 1