from typing import List


class PolishFlag:

    def sort_colors(self, nums: List[int]) -> None:
        """
        Approach: Three Pointers
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        left = 0
        right = len(nums) - 1
        pointer = 0

        while pointer <= right:

            if nums[pointer] == 0:
                nums[left], nums[pointer] = nums[pointer], nums[left]
                left += 1
                pointer += 1
            elif nums[pointer] == 2:
                nums[right], nums[pointer] = nums[pointer], nums[right]
                right -= 1
            else:
                pointer += 1
