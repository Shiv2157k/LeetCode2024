from typing import List
from math import inf


class Coins:

    def coin_change_v0(self, coins: List[int], amount: int) -> int:
        """
        Approach: Recursion with memo
        T: O(S * N)
        S: O(S)
        :param coins:
        :param amount:
        :return:
        """

        def recurse_with_memo(remain: int):

            if remain < 0:
                return -1
            if remain == 0:
                return 0
            if remain in memo:
                return memo[remain]

            min_count = inf

            for coin in coins:
                count = recurse_with_memo(remain - coin)
                if count == -1:
                    continue
                min_count = min(min_count, count + 1)
            memo[remain] = min_count if min_count != inf else -1
            return memo[remain]

        memo = {}
        return recurse_with_memo(amount)

    def coin_change_v1(self, coins: List[int], amount: int) -> int:
        """
        Approach: DP
        T: O(S * N)
        S: O(S)
        :param coins:
        :param amount:
        :return:
        """

        dp = [amount + 1] * (amount + 1)

        dp[0] = 0

        for curr_amount in range(1, amount + 1):
            for coin in coins:
                if curr_amount - coin < 0:
                    continue
                dp[curr_amount] = min(dp[curr_amount], dp[curr_amount - coin] + 1)
        return dp[amount] if dp[amount] != amount + 1 else -1
