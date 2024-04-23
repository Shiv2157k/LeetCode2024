class DistinctSubsequences:

    def numDistinctV2(self, s: str, t: str) -> int:
        """
        Approach: DP
        T: O(M*N)
        S: O(N)
        :param s:
        :param t:
        :return:
        """

        rows, cols = len(s), len(t)

        dp = [0] * cols

        for p1 in range(rows - 1, -1, -1):
            prev = 1
            for p2 in range(cols - 1, -1, -1):
                oldDp = dp[p2]

                if s[p1] == t[p2]:
                    dp[p2] += prev
                prev = oldDp
        return dp[0]

    def numDistinctV1(self, s: str, t: str) -> int:
        """
        Approach: DP
        T: O(M * N)
        S: O(M * N)
        :param s:
        :param t:
        :return:
        """

        rows, cols = len(s), len(t)

        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        for p1 in range(rows + 1):
            dp[p1][cols] = 1

        for p1 in range(rows - 1, -1, -1):
            for p2 in range(cols - 1, -1, -1):

                dp[p1][p2] = dp[p1 + 1][p2]

                if s[p1] == t[p2]:
                    dp[p1][p2] += dp[p1 + 1][p2 + 1]
        return dp[0][0]

    def numDistinctV0(self, s: str, t: str) -> int:
        """
        T: O(M * N)
        S: O(M * N)
        """
        sLen = len(s)
        tLen = len(t)

        def recurseWithMemo(p1: int, p2: int):

            if p1 == sLen or p2 == tLen or sLen - p1 < tLen - p2:
                return int(p2 == tLen)

            if (p1, p2) in memo:
                return memo[(p1, p2)]

            ans = recurseWithMemo(p1 + 1, p2)

            if s[p1] == s[p2]:
                ans += recurseWithMemo(p1 + 1, p2 + 1)

            memo[(p1, p2)] = ans
            return ans

        memo = {}
        return recurseWithMemo(0, 0)
