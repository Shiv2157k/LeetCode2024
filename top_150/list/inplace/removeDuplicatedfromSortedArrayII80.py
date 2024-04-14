from typing import List



class ArrayWithDuplicates:

    def removeDuplicates(self, nums: List[int]) -> (List[int], int):
        """
        Approach: Two Pointers
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        count = 0

        left, right = 0, 0
        n = len(nums)

        while right <= n - 1:
            
            if right < n - 1 and nums[right] == nums[right + 1]:
                count += 1
            else:
                count = 0

            if count < 2:
                nums[left] = nums[right]
                left += 1
            right += 1
        return nums, left


if __name__ == "__main__":
    arr = ArrayWithDuplicates()
    print(arr.removeDuplicates([1, 1, 1, 2, 2, 3]))