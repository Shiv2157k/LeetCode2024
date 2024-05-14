from typing import List


class PolishFlag:

    def sort_colors(self, nums: List[int]) -> List[int]:
        """
        Approach: Three Pointers
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        pointer = 0
        left = 0
        right = len(nums) - 1

        while left <= right:

            if nums[pointer] == 0:
                nums[pointer], nums[left] = nums[left], nums[pointer]
                left += 1
                pointer += 1
            elif nums[pointer] == 2:
                nums[pointer], nums[right] = nums[right], nums[pointer]
                right -= 1
            else:
                pointer += 1
        return nums
