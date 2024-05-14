from typing import List


class RotateArray:

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        # defensive programming against bad input
        k = k % n
        # reverse all the elements
        self.__reverse(nums, 0, n - 1)
        # reverse 0 - k - 1 elements
        self.__reverse(nums, 0, k - 1)
        # reverse k - n - 1 elements should give the desired results
        self.__reverse(nums, k, n - 1)

    def __reverse(self, nums: List[int], left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
