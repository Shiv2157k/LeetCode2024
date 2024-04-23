from typing import List


class ProductOfArray:

    def get_except_selfV1(self, nums: List[int]) -> List[int]:
        """
        Approach: Two Pointers Optimized no extra space
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        result: List[int] = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                result[i] = 1
            else:
                result[i] = result[i - 1] * nums[i - 1]

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * right
            right *= nums[i]
        return result

    def get_except_selfV0(self, nums: List[int]) -> List[int]:
        """
        Approach: Two Pointers
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        left: List[int] = []
        right: List[int] = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                left.append(1)
            else:
                left.append(left[i - 1] * nums[i - 1])

        for i in range(len(nums) - 1, -1, -1):

            if i == len(nums) - 1:
                right[i] = 1
            else:
                right[i] = right[i + 1] * nums[i + 1]

        result: List[int] = []
        for i in range(len(nums)):
            result.append(left[i] * right[i])
        return result
