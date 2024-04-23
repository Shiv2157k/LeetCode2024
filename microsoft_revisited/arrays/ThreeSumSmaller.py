from typing import List


class ThreeSumSmaller:

    def threeSumSmaller(self, nums: List[int], target: int) -> int:

        nums.sort()
        totalSmaller = 0

        for index in range(len(nums)):
            totalSmaller += self.twoSumSmaller(nums, index, target)
        return totalSmaller

    def twoSumSmaller(self, nums: List[int], index: int, target: int) -> int:

        totalSmaller = 0
        left = index + 1
        right = len(nums) - 1
        while left < right:
            if nums[index] + nums[left] + nums[right] < target:
                totalSmaller += right - left
                left += 1
            else:
                right -= 1
        return totalSmaller
