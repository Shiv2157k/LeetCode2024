from typing import List


class DutchNationalFlag:

    def correct_format(self, nums: List[List[int]]) -> List[List[int]]:
        """
        Approach: One Pass
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """
        left = curr_pointer = 0
        right = len(nums) - 1
        while curr_pointer <= right:
            if nums[curr_pointer] == 0:
                # swap
                nums[left], nums[curr_pointer] = nums[curr_pointer], nums[left]
                left += 1
                curr_pointer += 1
            elif nums[curr_pointer] == 2:
                # swap
                nums[right], nums[curr_pointer] = nums[curr_pointer], nums[right]
                right -= 1
            else:  # 1
                curr_pointer += 1
        return nums


if __name__ == "__main__":
    flag = DutchNationalFlag()
    print(flag.correct_format([1, 1, 0, 2, 2, 2]))
    print(flag.correct_format([1, 0, 2]))
    print(flag.correct_format([2, 0, 1]))
    print(flag.correct_format([2, 0, 0, 1]))
    print(flag.correct_format([1, 0, 1]))
