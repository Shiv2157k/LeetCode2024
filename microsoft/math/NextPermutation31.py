from typing import List


class NextPermutation:

    def getNext(self, nums: List[int]):

        p1 = len(nums) - 2

        while p1 >= 0 and nums[p1 + 1] <= nums[p1]:
            p1 -= 1

        if p1 >= 0:
            p2 = len(nums) - 1
            while nums[p2] <= nums[p1]:
                p2 -= 1
            nums[p1], nums[p2] = nums[p2], nums[p1]

        left = p1 + 1
        right = len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
