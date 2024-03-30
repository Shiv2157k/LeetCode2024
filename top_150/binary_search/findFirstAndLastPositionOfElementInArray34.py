from typing import List


class Positions:

    def findFirstAndLast(self, nums: List[int], target: int) -> List[int]:
        """
        Approach: Binary Search
        T: O(log N)
        S: O(1)
        :param nums:
        :param target:
        :return:
        """

        # Make two calls of binary search for the leftMost target and rightMost target
        leftMost = self._binarySearch(nums, target, True)
        if leftMost == -1:
            return [-1, -1]
        rightMost = self._binarySearch(nums, target)

        return [leftMost, rightMost]

    def _binarySearch(self, nums: List[int], target: int, isLeft: bool = False) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:

            pivot = left + (right - left) // 2

            if nums[pivot] == target:

                if isLeft:
                    if left == pivot or nums[pivot] != nums[pivot - 1]:
                        return pivot
                    else:
                        right = pivot - 1
                else:
                    if right == pivot or nums[pivot] != nums[pivot + 1]:
                        return pivot
                    else:
                        left = pivot + 1
            elif nums[pivot] > target:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1


if __name__ == "__main__":
    position = Positions()
    print(position.findFirstAndLast([5, 7, 7, 8, 8, 10], 8))
    print(position.findFirstAndLast([5, 7, 7, 8, 8, 10], 9))
    print(position.findFirstAndLast([9, 9, 9], 9))
