from typing import List



class ProductOfArrayExceptSelf:


    def getProductArrayV0(self, nums: List[int]) -> List[int]:
        """
        Approach: Two Arrays
        T: O(N + N)
        S: O(N + N)
        :param nums:
        :return:
        """
        length = len(nums)
        left = [0] * length
        left[0] = 1

        for i in range(1, length):
            left[i] = left[i - 1] * nums[i - 1]

        right = [0] * length
        right[length - 1] = 1

        for i in range(length - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        productArr = []

        for i in range(length):
            productArr.append(left[i] * right[i])
        return productArr

    def getProductArrayV1(self, nums: List[int]) -> List[int]:
        """
        Approach: No extra memory
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        length = len(nums)
        productArr = [0] * length
        productArr[0] = 1

        for i in range(1, length):
            productArr[i] = productArr[i - 1] * nums[i - 1]

        right = 1
        for i in range(length - 1, -1, -1):
            productArr[i] = productArr[i] * right
            right *= nums[i]

        return productArr

