from typing import List


class PositiveInteger:

    def getFirstMissingV1(self, nums: List[int]) -> int:
        """
        Approach: Cycle Sort
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        size = len(nums)

        index = 0
        while index < size - 1:
            pos = nums[index] - 1
            if 0 < nums[index] <= size and nums[index] != nums[pos]:
                # swap
                nums[index], nums[pos] = nums[pos], nums[index]
            else:
                index += 1

        for index in range(size):
            if nums[index] != index + 1:
                return index + 1
        return size + 1

    def getFirstMissingV0(self, nums: List[int]) -> int:
        """
        Approach: Index as Hash Key
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        size = len(nums)

        if 1 not in nums:
            return 1

        for index in range(size):
            if nums[index] <= 0 or nums[index] > size:
                nums[index] = 1

        for index in range(size):

            val = abs(nums[index])

            if val == size:
                nums[0] = - abs(nums[0])
            else:
                nums[val] = - abs(nums[val])

        for index in range(1, size):
            if nums[index] > 0:
                return index

        if nums[0] > 0:
            return size

        return size + 1


if __name__ == "__main__":
    posInteger = PositiveInteger()
    print(posInteger.getFirstMissingV0([3, 4, -1, 1]))
    print(posInteger.getFirstMissingV1([3, 4, -1, 1]))
    print(posInteger.getFirstMissingV0([1, 2, 3]))
    print(posInteger.getFirstMissingV1([1, 2, 3]))
    print(posInteger.getFirstMissingV0([1, 2, 4]))
    print(posInteger.getFirstMissingV1([1, 2, 4]))
