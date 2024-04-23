from typing import List


class SortColors:

    def sortColors(self, nums: List[int]) -> None:
        """
        Approach: Two Pointers
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        left, right = 0, len(nums) - 1
        pointer = 0

        while pointer <= right:
            if nums[pointer] == 0:
                nums[pointer], nums[left] = nums[left], nums[pointer]
                left += 1
                pointer += 1
            elif nums[pointer] == 2:
                nums[pointer], nums[right] = nums[right], nums[pointer]
                right -= 1
            else:
                pointer += 1
