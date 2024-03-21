from typing import List


class ProductSubArray:

    def max_product(self, nums: List[int]) -> int:
        """
        Approach: DP
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        if len(nums) == 0:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = nums[0]

        for index in range(1, len(nums)):
            temp_max = max(nums[index], max_so_far * nums[index], min_so_far * nums[index])
            min_so_far = min(nums[index], min_so_far * nums[index], max_so_far * nums[index])
            max_so_far = temp_max
            result = max(max_so_far, result)
        return result


if __name__ == "__main__":
    product_sub = ProductSubArray()
    print(product_sub.max_product([2, 3, -2, 4]))
    print(product_sub.max_product([2, -5, 3, 1, -4, 0, -10, 2, 8]))
