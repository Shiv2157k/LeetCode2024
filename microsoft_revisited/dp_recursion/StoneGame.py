from typing import List


class StoneGame:

    def stone_game(self, piles: List[int]) -> bool:
        """
        Approach: DP
        T: O(N)
        S: O(N)
        :param piles:
        :return:
        """
        n = len(piles)
        dp = [0] * (n // 2 + 1)

        for i in range(1, n // 2 + 1):
            dp[i] = dp[i - 1] + max(piles[i] - piles[n - i], piles[n - 1] - piles[i])
        return dp[n // 2] > 0
