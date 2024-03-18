from typing import List


class SubArray:

    def max_sum_sub_array_v1(self, nums: List[int]) -> int:
        """
        Approach: DP
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """
        max_sum = curr_sum = nums[0]
        for num in nums[1:]:
            curr_sum = max(curr_sum, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
        return max_sum

    def max_sum_sub_array_v0(self, nums: List[int]) -> int:
        """
        Approach: DP (My Style)
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """
        size = len(nums)
        dp = [float("-inf")] * size
        dp[0] = max_sum = nums[0]

        for index in range(1, size):
            dp[index] = max(nums[index], dp[index - 1] + nums[index])
            max_sum = max(max_sum, dp[index])
        return max_sum


if __name__ == "__main__":
    sub_array = SubArray()
    print(sub_array.max_sum_sub_array_v0([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(sub_array.max_sum_sub_array_v0([1]))
    print(sub_array.max_sum_sub_array_v0([5, 4, -1, 7, 8]))
    print("___**___")
    print(sub_array.max_sum_sub_array_v0([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(sub_array.max_sum_sub_array_v0([1]))
    print(sub_array.max_sum_sub_array_v0([5, 4, -1, 7, 8]))
