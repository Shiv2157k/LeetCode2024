class DistinctSubsequences:

    def num_distinct_v2(self, s: str, t: str) -> int:
        """
        Approach: DP with space optimized
        T: O(ST)
        S: O(N)
        :param s:
        :param t:
        :return:
        """

        s_len = len(s)
        t_len = len(t)

        dp = [0] * t_len

        for p1 in range(s_len - 1, -1, -1):
            prev = 1
            for p2 in range(t_len - 1, -1, -1):
                temp = dp[p2]
                if s[p1] == t[p2]:
                    dp[p2] += prev
                prev = temp
        return dp[0]

    def num_distinct_v1(self, s: str, t: str) -> int:
        """
        Approach: DP
        T: O(ST)
        S: O(ST)
        :param s:
        :param t:
        :return:
        """

        s_len = len(s)
        t_len = len(t)

        dp = [[0] * (t_len + 1) for _ in range(s_len + 1)]

        # mask the last column with 1
        for p1 in range(t_len + 1):
            dp[p1][t_len] = 1

        for p1 in range(s_len - 1, -1, -1):
            for p2 in range(t_len - 1, -1, -1):
                dp[p1][p2] += dp[p1 + 1][p2]
                if s[p1] == t[p2]:
                    dp[p1][p2] += dp[p1 + 1][p2 + 1]
        return dp[0][0]

    def num_distinct_v0(self, s: str, t: str) -> int:
        """
        Approach: DP with memo
        T: O(ST)
        S: O(ST)
        :param s:
        :param t:
        :return:
        """

        s_len = len(s)
        t_len = len(t)

        def helper(p1: int, p2: int) -> int:

            if p1 == s_len or p2 == s_len or s_len - p1 < t_len - p2:
                return int(p2 == t_len)

            if (p1, p2) in memo:
                return memo[(p1, p2)]

            ans = helper(p1 + 1, p2)
            if s[p1] == t[p2]:
                ans += helper(p1 + 1, p2 + 1)
            memo[(p1, p2)] = ans
            return memo[(p1, p2)]

        memo = {}
        return helper(0, 0)
