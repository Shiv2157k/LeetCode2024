from typing import List


class ThreeSum:

    def three_sum(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Two Pointers
        t: O(N^2)
        S: O(1)
        :param nums:
        :return:
        """

        nums.sort()
        result = []

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if i == 0 or nums[i] != nums[i - 1]:
                self.__get_three_sum_pairs(nums, i, result)

    def __get_three_sum_pairs(self, nums: List[int], fixed_ptr: int, result: List[List[int]]) -> None:
        left = fixed_ptr + 1
        right = len(nums) - 1

        while left < right:
            curr_sum = nums[fixed_ptr] + nums[left] + nums[right]

            if curr_sum == 0:
                result.append([nums[fixed_ptr], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
            elif curr_sum > 0:
                right -= 1
            else:
                left += 1
