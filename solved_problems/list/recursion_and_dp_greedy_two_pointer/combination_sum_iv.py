from typing import List


class CombinationSumIV:

    def get_total_combinations_v1(self, nums: List[int], target: int) -> int:
        """
        Approach: DP (Bottom UP)
        T: O(T * N)
        S: O(T)
        :param nums:
        :param target:
        :return:
        """
        dp = [0] * (target + 1)
        dp[0] = 1

        for curr_target in range(target + 1):
            for num in nums:
                if curr_target - num >= 0:
                    dp[curr_target] += dp[curr_target - num]
        return dp[target]

    def get_total_combinations_v0(self, nums: List[int], target: int) -> int:
        """
        Approach: Recursion with memoization (top down)
        T: O(T * N)
        S: O(T)
        :param nums:
        :param target:
        :return:
        """
        memo = {}

        def combinations(remain_target: int) -> int:
            # base case
            if remain_target == 0:
                return 1
            if remain_target in memo:
                return memo[remain_target]

            result = 0
            for num in nums:
                if remain_target - num >= 0:
                    result += combinations(remain_target - num)
            memo[remain_target] = result
            return result

        return combinations(target)


if __name__ == "__main__":
    combination_sum_iv = CombinationSumIV()
    print(combination_sum_iv.get_total_combinations_v0(
        [1, 2, 3], 4
    ))
    print(combination_sum_iv.get_total_combinations_v1(
        [1, 2, 3], 4
    ))
    print(combination_sum_iv.get_total_combinations_v0(
        [1, 2, 1], 2
    ))
    print(combination_sum_iv.get_total_combinations_v1(
        [1, 2, 1], 2
    ))