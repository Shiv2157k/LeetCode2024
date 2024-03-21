from typing import List


class Product:

    def of_array_except_self_v1(self, nums: List[int]) -> List[int]:
        """
        Approach: Left Right Space Optimization
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        length = len(nums)

        answer = [0] * length
        answer[0] = 1

        for index in range(1, length):
            answer[index] = answer[index - 1] * nums[index - 1]

        right = 1
        for index in range(length - 1, -1, -1):
            answer[index] = answer[index] * right
            right *= nums[index]
        return answer

    def of_array_except_self_v0(self, nums: List[int]) -> List[int]:
        """
        Approach: left and right
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """
        length = len(nums)
        left, right = [0] * len(nums), [0] * len(nums)
        left[0], right[-1] = 1, 1

        for index in range(1, len(nums)):
            left[index] = left[index - 1] * nums[index - 1]

        for index in range(length - 2, -1, -1):
            right[index] = right[index + 1] * nums[index + 1]

        answer = []
        for index in range(length):
            answer.append(left[index] * right[index])
        return answer


if __name__ == "__main__":
    product = Product()
    print(product.of_array_except_self_v0([1,2,3,4]))
    print(product.of_array_except_self_v1([1, 2, 3, 4]))