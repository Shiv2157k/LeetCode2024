from typing import List


class UniquePaths:

    def uniquePathsV0(self, m: int, n: int) -> int:

        if m == 1 or n == 1:
            return 1

        return self.uniquePathsV0(m - 1, n) + self.uniquePathsV0(m, n - 1)

    def uniquePathsV1(self, m: int, n: int) -> int:

        dp = [[1] * n for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[m - 1][n - 1]
