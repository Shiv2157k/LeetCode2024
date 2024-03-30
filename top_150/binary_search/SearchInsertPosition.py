from typing import List


class InsertPosition:

    def search(self, nums: List[int], target: int) -> int:
        """
        Approach: Binary Search
        T: O(log N)
        S: O()
        :param nums:
        :param target:
        :return:
        """

        left, right = 0, len(nums) - 1

        while left <= right:

            pivot = left + (right - left) // 2

            if nums[pivot] == target:
                return pivot
            elif nums[pivot] > target:
                right = pivot - 1
            else:
                left = pivot + 1
        return left


if __name__ == "__main__":
    insertPosition = InsertPosition()
    print(insertPosition.search([1, 3, 5, 6], 5))
    print(insertPosition.search([1, 3, 5, 6], 2))
    print(insertPosition.search([1, 3, 5, 6], 7))
