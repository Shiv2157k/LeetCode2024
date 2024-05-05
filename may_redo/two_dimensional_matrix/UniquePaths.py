from typing import List


class UniquePaths:

    def total_unique_paths_v0(self, m: int, n: int) -> int:
        """
        Approach: Recursion
        T: O(NM)
        S: O(MN)
        :param m:
        :param n:
        :return:
        """

        if m == 1 or n == 1:
            return 1
        return self.total_unique_paths_v0(m - 1, n) + self.total_unique_paths_v0(m, n - 1)

    def total_unique_paths_v1(self, m: int, n: int) -> int:
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
