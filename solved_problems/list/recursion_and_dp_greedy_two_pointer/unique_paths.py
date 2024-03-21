class Path:

    def number_of_unique_v0(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.number_of_unique_v0(m - 1, n) + self.number_of_unique_v0(m, n - 1)

    def number_of_unique_v1(self, m: int, n: int) -> int:
        """
        Approach: DP
        T: O(M * N)
        S: O(M * N)
        :param m:
        :param n:
        :return:
        """

        dp = [[1] * n for _ in range(m)]
        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        return dp[m - 1][n - 1]


if __name__ == "__main__":
    path = Path()
    print(path.number_of_unique_v0(3, 7))
    print(path.number_of_unique_v1(3, 7))
