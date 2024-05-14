class UniquePaths:

    def unique_paths(self, m: int, n: int) -> int:
        """
        Approach: DP
        T: O(MN)
        S: O(MN)
        :param m:
        :param n:
        :return:
        """
        dp = [[1] * n for _ in range(m)]
        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        return dp[-1][-1]
