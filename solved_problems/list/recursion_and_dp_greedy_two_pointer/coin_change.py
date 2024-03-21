from typing import List, Dict


class CoinChange:

    def minimum_coins_needed_v2(self, coins: List[int], amount: int) -> int:
        """
        Approach: DP
        T: O(S * N)
        S: O(N)
        :param coins:
        :param amount:
        :return:
        """
        # our dp store will be amount + 1 in length and value
        dp = [(amount + 1) for _ in range(amount + 1)]
        dp[0] = 0
        for curr_amount in range(1, amount + 1):
            for coin in coins:
                if curr_amount - coin < 0:
                    continue
                dp[curr_amount] = min(dp[curr_amount], dp[curr_amount - coin] + 1)
        return dp[amount] if dp[amount] != amount + 1 else -1

    def minimum_coins_needed_v1(self, coins: List[int], amount: int) -> int:
        """
        Approach: Recursion with memo
        T: O(S * N)
        S: O(N)
        :param coins:
        :param amount:
        :return:
        """
        memo = {}
        return self.recurse_with_memo(coins, amount, memo)

    def recurse_with_memo(self, coins: List[int], amount: int, memo: Dict ):

        # bases cases
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if amount in memo:
            return memo[amount]

        min_coins = float("inf")
        for coin in coins:
            count = self.recurse_with_memo(coins, amount - coin, memo)
            if count == -1:
                continue
            min_coins = min(min_coins, count + 1)
        memo[amount] = min_coins if min_coins != float("inf") else -1
        return memo[amount]

    def minimum_coins_needed_v0(self, coins: List[int], amount: int) -> int:
        """
        Approach: Recursion
        T: O(S^N)
        S: O(N)
        :param coins:
        :param amount:
        :return:
        """
        return self.recursion_helper(coins, amount)

    def recursion_helper(self, coins: List[int], remaining_amount: int) -> int:
        # base cases
        if remaining_amount < 0:
            return -1
        if remaining_amount == 0:
            return 0

        min_coins = float("inf")
        for coin in coins:
            count = self.recursion_helper(coins, remaining_amount - coin)
            if count == -1:
                continue
            min_coins = min(min_coins, count + 1)
        return min_coins if min_coins != float("inf") else -1
