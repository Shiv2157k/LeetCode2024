from typing import List


class FirstMissingPositive:

    def first_missing_positive_v0(self, nums: List[int]) -> int:
        """
        Approach: Hash Bucket
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        # validation
        if 1 not in nums:
            return 1

        size = len(nums)

        # Step 1: Flip negatives, equal to 0 and greater than size to 1
        for i in range(size):

            if nums[i] <= 0 or nums[i] > size:
                nums[i] = 1

        # Step 2: Hash with val as index

        for i in range(size):

            val = abs(nums[i])

            if val == size:
                nums[0] = -abs(nums[0])
            else:
                nums[val] = -abs(nums[val])

        for i in range(1, size):
            if nums[i] > 1:
                return i

        if nums[0] > 0:
            return size
        return size + 1
