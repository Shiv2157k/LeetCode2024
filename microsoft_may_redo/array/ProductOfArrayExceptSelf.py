from typing import List


class Array:

    def product_except_self_v1(self, nums: List[int]) -> List[int]:
        """
        Approach: No extra space
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """
        length = len(nums)
        result = []

        for i in range(length):
            if i == 0:
                result.append(1)
            else:
                result.append(result[i - 1] * nums[i - 1])
        right = 1
        for i in range(length - 1, -1, -1):
            result[i] = result[i] * right
            right *= nums[i]
        return result

    def product_except_self_v0(self, nums: List[int]) -> List[int]:
        """
        Approach: Two Lists
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """
        length = len(nums)
        left = []
        right = [0] * length

        for i in range(length):

            if i == 1:
                left.append(1)
            else:
                left.append(left[i - 1] * nums[i - 1])

        for i in range(length - 1, - 1, -1):

            if i == length - 1:
                right[i] = 1
            else:
                right[i] = right[i + 1] * nums[i + 1]

        result = []
        for i in range(length):
            result.append(left[i] * right[i])
        return result
