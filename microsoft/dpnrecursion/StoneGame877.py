from typing import List


class StoneGame:

    def stoneGameV2(self, piles: List[int]) -> bool:
        return True

    def stoneGameV0(self, piles: List[int]) -> bool:
        """
        Approach: DP and Greedy
        T: O(N)
        S: O(N)
        :param piles:
        :return:
        """

        n = len(piles)
        dp = [0] * (n // 2 + 1)

        for i in range(1, n // 2 + 1):
            dp[i] = dp[i - 1] + max(piles[i] - piles[n - 1], piles[n - i] - piles[i])
        return dp[n // 2] > 0

    def stoneGameV0(self, piles: List[int]) -> bool:
        """
        Approach: DP
        T: O(N^2)
        S: O(N^2)
        :param piles:
        :return:
        """

        n = len(piles)
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        for size in range(1, n + 1):
            for i in range(0, n - size + 1):

                j = i + size - 1
                parity = (j + i + n) % 2

                if parity == 1:
                    dp[i + 1][j + 1] = max(piles[i] + dp[i + 2][j + 1], piles[j] + dp[i + 1][j])
                else:
                    dp[i + 1][j + 1] = min(-piles[i] + dp[i + 2][j + 1], -piles[j] + dp[i + 1][j])
        return dp[1][n] > 0
