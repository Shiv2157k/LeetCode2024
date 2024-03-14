from typing import List


class SortedList:

    def remove_duplicates(self, nums: List[int]) -> int:
        """
        Approach: Two Pointer
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """
        size = len(nums)
        # determines the unique numbers
        pointer = 1

        for i in range(1, size):
            # check side index value is same or not
            if nums[i] != nums[i - 1]:
                # move/ replace the unique number to the right index
                nums[pointer] = nums[i]
                # increment the pointer
                pointer += 1
        return pointer


if __name__ == "__main__":
    sortedList = SortedList()
    print(sortedList.remove_duplicates([1, 1, 2, 2, 3, 3]))
    print(sortedList.remove_duplicates([1, 1, 3, 4, 5]))
    print(sortedList.remove_duplicates([1, 1, 2, 2, 2, 3, 3, 3]))
    print(sortedList.remove_duplicates([1, 2, 2, 3, 3, 4, 5, 5]))
