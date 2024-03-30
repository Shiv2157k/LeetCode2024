from typing import List


class SortedArray:


    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Approach: Two Pointer
        :param nums:
        :return:
        """
        size = len(nums)
        insertIndex = 1

        for index in range(1, size):

            if nums[index] != nums[index - 1]:
                nums[insertIndex] = nums[index]
                insertIndex += 1
        return insertIndex


if __name__ == "__main__":
    sortedArray = SortedArray()
    print(sortedArray.removeDuplicates([1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))