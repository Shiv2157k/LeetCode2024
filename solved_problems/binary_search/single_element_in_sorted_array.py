from typing import List


class SortedArray:

    def findSingleElement_(self, nums: List[int]) -> int:
        """
        Approach: Binary Search with even indexes
        T: O(log N/2)
        S: O(1)
        :param nums:
        :return:
        """

        left, right = 0, len(nums) - 1

        while left < right:

            pivot = left + (right - left) // 2

            # always pivot needs to be even indexed
            if pivot % 2 == 1:
                pivot -= 1

            # move left to even index
            if nums[pivot] == nums[pivot + 1]:
                left = pivot + 2
            else:
                right = pivot
        return nums[left]

    def findSingleElement(self, nums: List[int]) -> int:
        """
        Approach: Binary Search
        T: O(log N)
        S: O(1)
        Case 1: if halves are both even, mid's partner is to right
         0 1 2 3 4 5 6 7 8 -> index
        |1|1|4|4|5|5|6|8|8|
        l        m       r
        l = mid + 2
        Case 2: if halves are odd and mid's partner is to right
        0 1 2 3 4 5 6 7 8 -> index
        |1|1|4|5|5|6|6|8|8|9|9|
        l          m         r
        h = mid - 1
        Case 3: if halves are even and mid's partner is to left
        0 1 2 3 4 5 6 7 8 -> index
        |1|1|4|5|5|6|6|8|8|9|9|
        l            m       r
        hi = mid - 2
        Case 4: if halves are odd and mid's partner is to left
        0 1 2 3 4 5 6 7 8 -> index
        |1|1|4|4|5|5|6|8|8|
        l      m         r
        l = mid - 1
        :param nums:
        :return:
        """
        left, right = 0, len(nums) - 1

        while left < right:
            pivot = left + (right - left) // 2
            halves_are_even = (right - pivot) % 2 == 0

            # pivots partner is to right
            if nums[pivot] == nums[pivot + 1]:
                if halves_are_even:
                    left = pivot + 2
                else:
                    right = pivot - 1
            # pivot partner is to left
            elif nums[pivot] == nums[pivot - 1]:
                if halves_are_even:
                    right = pivot - 2
                else:
                    left = pivot + 1
            else:
                return nums[pivot]
        return nums[left]


if __name__ == "__main__":
    sortedArray = SortedArray()
    print(sortedArray.findSingleElement([1, 1, 4, 4, 5, 6, 6, 7, 7]))
    print(sortedArray.findSingleElement([1, 1, 4, 4, 5, 5, 6, 7, 7]))
    print(sortedArray.findSingleElement([1, 1, 4, 5, 5, 6, 6, 7, 7]))
    print("-*-")
    print(sortedArray.findSingleElement([1, 1, 4, 4, 5, 6, 6, 7, 7]))
    print(sortedArray.findSingleElement([1, 1, 4, 4, 5, 5, 6, 7, 7]))
    print(sortedArray.findSingleElement([1, 1, 4, 5, 5, 6, 6, 7, 7]))


