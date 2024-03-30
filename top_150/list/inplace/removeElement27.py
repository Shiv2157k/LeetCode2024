from typing import List


class ArrayList:

    def removeElement(self, nums: List[int], val: int) -> int:
        writer = 0

        for reader, currVal in enumerate(nums):

            if currVal != val:
                nums[writer] = currVal
                writer += 1
        return writer

    def removeElementV1(self, nums: List[int], val: int) -> int:

        left, right = 0, len(nums)

        while left < right:

            if nums[left] == val:
                nums[left] = nums[right - 1]
                right -= 1
            else:
                left += 1
        return right


if __name__ == "__main__":
    arr = ArrayList()
    print(arr.removeElement([3, 2, 2, 3], 3))
    print(arr.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))

    print(arr.removeElementV1([3, 2, 2, 3], 3))
    print(arr.removeElementV1([0, 1, 2, 2, 3, 0, 4, 2], 2))
