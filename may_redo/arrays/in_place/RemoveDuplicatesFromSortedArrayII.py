from typing import List


class SortedArrayII:

    def remove_duplicates_v1(self, nums: List[int]) -> int:

        count = 1
        writer = 1

        for reader in range(1, len(nums)):

            if nums[reader - 1] == nums[reader]:
                count += 1
            else:
                count = 1
            if count <= 2:
                nums[writer] = nums[reader]
                writer += 1
        return writer

    def remove_duplicated_v0(self, nums: List[int]) -> int:
        """
        Approach: Two Pointer
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """
        counter = 1
        left = 1
        right = 1

        while right < len(nums):

            if nums[right - 1] == nums[right]:
                counter += 1
            else:
                counter = 1

            if counter <= 2:
                nums[left] = nums[right]
                left += 1
            right += 1
        return left

