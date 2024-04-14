from typing import List



class PolishFlag:


    def sortColors(self, nums: List[int]) -> List[int]:
        """
        Approach: Two / Three Pointer
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """
        length = len(nums)
        left, right = 0, length - 1
        pointer = 0

        while pointer <= right:
            # if pointer is pointing at 0 val swap left <-> pointer values
            # increment left and right pointer
            if nums[pointer] == 0:
                nums[pointer], nums[left] = nums[left], nums[pointer]
                left += 1
                pointer += 1
            # if pointer is pointing at 2 val swap right <-> pointer values
            # decrement right pointer
            elif nums[pointer] == 2:
                nums[pointer], nums[right] = nums[right], nums[pointer]
                right -= 1
            else:  # otherwise increment pointer
                pointer += 1
        return nums


if __name__ == "__main__":
    polishFlag = PolishFlag()
    print(polishFlag.sortColors([2, 0, 2, 1, 1, 0]))
    print(polishFlag.sortColors([2, 0, 1]))
