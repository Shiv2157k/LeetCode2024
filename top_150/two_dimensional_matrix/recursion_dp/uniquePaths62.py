


class UniquePath:


    def totalV0(self, m: int, n: int) -> int:
        """
        Approach: Recursion
        T: O(MN)
        S: O(MN)
        :param m:
        :param n:
        :return:
        """

        if m == 1 or n == 1:
            return 1

        return self.totalV0(m - 1, n) + self.totalV0(m, n - 1)

    def totalV1(self, m: int, n: int) -> int:
        """
        Approach: Iterative
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


if __name__ == "__main__":
    uniquePath = UniquePath()
    print(uniquePath.totalV0(3, 7))
    print(uniquePath.totalV1(3, 7))