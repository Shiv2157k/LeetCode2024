from typing import List


class ArrayList:

    def maxSubArraySumV1(self, nums: List[int]) -> int:
        """
        Approach: Greedy
        T: O(N)
        S: O(1)
        :param nums:
        :return:
        """

        length = len(nums)
        if length == 1:
            return nums[0]

        maxSum = nums[0]
        currSum, prevSum = nums[0], nums[0]

        for index in range(1, length):
            currSum = max(nums[index] + currSum, nums[index])
            maxSum = max(maxSum, currSum)
        return maxSum

    def maxSubArraySumV0(self, nums: List[int]) -> int:
        """
        Approach: DP
        T: O(N)
        S: O(N)
        :param nums:
        :return:
        """

        length = len(nums)

        if length == 1:
            return nums[0]

        dp = [float("-inf")] * length
        dp[0] = nums[0]
        maxSum = nums[0]

        for index in range(1, length):
            dp[index] = max(dp[index - 1] + nums[index], nums[index])
            if dp[index] > maxSum:
                maxSum = dp[index]
        return maxSum


if __name__ == "__main__":
    arrList = ArrayList()
    print(arrList.maxSubArraySumV0([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(arrList.maxSubArraySumV0([5, 4, -1, 7, 8]))

    print(arrList.maxSubArraySumV1([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(arrList.maxSubArraySumV1([5, 4, -1, 7, 8]))
