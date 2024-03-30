from typing import List


class NumberList:

    def missingNumberV1(self, nums: List[int]) -> int:
        """
        Approach: Guage Formula
        T: O (N)
        S: O(1)
        :param nums:
        :return:
        """
        expectedSum = len(nums) * (len(nums) + 1) // 2
        actualSum = 0
        for num in nums:
            actualSum += num
        return expectedSum - actualSum

    def missingNumberV0(self, nums: List[int]) -> int:
        """
        Approach: Bit Manipulation
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """
        missing = len(nums)

        for index, num in enumerate(nums):
            missing = missing ^ index ^ num
        return missing


if __name__ == "__main__":
    numberList = NumberList()
    print(numberList.missingNumberV0([1, 3, 0]))
    print(numberList.missingNumberV0([9, 6, 4, 2, 3, 5, 7, 0, 1]))

    print(numberList.missingNumberV1([0, 3, 2]))
    print(numberList.missingNumberV1([9, 6, 4, 2, 3, 5, 7, 0, 1]))
