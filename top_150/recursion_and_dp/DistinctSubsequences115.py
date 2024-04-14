class DistinctSubsequences:

    def numDistinctV2(self, s: str, t: str) -> int:
        """
        Approach: DP with O(N)
        T: O(M *N)
        S: O(N)
        :param s:
        :param t:
        :return:
        """
        S, T = len(s), len(t)
        dp = [0] * T

        for p1 in range(S - 1, -1, -1):
            prev = 1
            for p2 in range(T - 1, -1, -1):
                oldDp = dp[p2]

                if s[p1] == t[p2]:
                    dp[p2] += prev

                prev = oldDp
        return dp[0]

    def numDistinctV1(self, s: str, t: str) -> int:
        """
        Approach: DP bottom up
        T: O(M * N)
        S: O(M * N)
        :param s:
        :param t:
        :return:
        """

        S, T = len(s), len(t)
        dp = [[0] * (T + 1) for _ in range(S + 1)]

        for p1 in range(S + 1):
            dp[p1][T] = 1

        for p1 in range(S - 1, -1, -1):
            for p2 in range(T - 1, -1, -1):

                dp[p1][p2] = dp[p1 + 1][p2]

                if s[p1] == t[p2]:
                    dp[p1][p2] += dp[p1 + 1][p2 + 1]
        return dp[0][0]

    def numDistinctV0(self, s: str, t: str) -> int:
        """
        Approach: DP top down
        T: O(M * N)
        S: O(M * N)
        :param s:
        :param t:
        :return:
        """

        def recurseWithMemo(p1: int, p2: int) -> int:

            S, T = len(s), len(t)
            # base cases
            if p1 == S or p2 == T or S - p1 < T - p2:
                return int(p2 == T)

            if (p1, p2) in memo:
                return memo[(p1, p2)]

            ans = recurseWithMemo(p1 + 1, p2)

            if s[p1] == t[p2]:
                ans += recurseWithMemo(p1 + 1, p2 + 1)

            memo[(p1, p2)] = ans
            return ans

        memo = dict()
        return recurseWithMemo(0, 0)


if __name__ == "__main__":
    distinctSubSequence = DistinctSubsequences()
    print(distinctSubSequence.numDistinctV0(s="rabbbit", t="rabbit"))
    print(distinctSubSequence.numDistinctV1(s="rabbbit", t="rabbit"))
    print(distinctSubSequence.numDistinctV2(s="rabbbit", t="rabbit"))
