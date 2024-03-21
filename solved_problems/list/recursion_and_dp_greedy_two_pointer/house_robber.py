from typing import List


class Robber:

    def max_robbed_v1(self, houses: List[int]) -> int:
        """
        Approach: DP
        T: O(N)
        S: O(N)
        :param houses:
        :return:
        """
        if len(houses) == 1:
            return houses[0]

        dp = [0] * len(houses)
        dp[0] = houses[0]
        dp[1] = max(dp[0], houses[1])

        for num in range(2, len(houses)):
            dp[num] = max(dp[num - 1], dp[num - 2] + houses[num])
        return dp[-1]

    def max_robbed_v0(self, houses: List[int]) -> int:
        """
        Approach: DP (top_down)
        S: O(N)
        T: O(N)
        :param houses:
        :return:
        """
        memo = {}

        def recurse_with_memo(curr_house: int) -> int:
            if curr_house == 0:
                return houses[curr_house]
            if curr_house == 1:
                return max(houses[curr_house], houses[curr_house - 1])
            if curr_house in memo:
                return memo[curr_house]

            memo[curr_house] = max(recurse_with_memo(curr_house - 1),
                                   recurse_with_memo(curr_house - 2) + houses[curr_house])
            return memo[curr_house]

        return recurse_with_memo(len(houses) - 1)


if __name__ == "__main__":
    robber = Robber()
    print(robber.max_robbed_v0([1, 2, 3, 1]))
    print(robber.max_robbed_v1([1, 2, 3, 1]))
