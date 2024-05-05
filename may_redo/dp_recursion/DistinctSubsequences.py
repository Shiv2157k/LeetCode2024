from typing import List


class DistinctSubSequences:

    def num_distinct_v2(self, s: str, t: str) -> int:
        """
        Approach: DP O(N) Space
        T: O(M * N)
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

                old_dp = dp[p2]
                if s[p1] == t[p2]:
                    dp[p2] += prev
                prev = old_dp
        return dp[0]

    def num_distinct_v1(self, s: str, t: str) -> int:
        """
        Approach: DP
        T: O(N * M)
        S: O(N * M)
        :param s:
        :param t:
        :return:
        """

        rows = len(s)
        cols = len(t)

        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        for p1 in range(rows + 1):
            dp[p1][cols] = 1

        for p1 in range(rows - 1, -1, -1):
            for p2 in range(cols - 1, -1, -1):
                dp[p1][p2] += dp[p1 + 1][p2]
                if s[p1] == t[p2]:
                    dp[p1][p2] += dp[p1 + 1][p2 + 1]
        return dp[0][0]

    def num_distinct_v0(self, s: str, t: str) -> int:
        """
        Approach: Recurse with Memo
        T: O(N)
        S: O(N)
        :param s:
        :param t:
        :return:
        """

        s_len = len(s)
        t_len = len(t)

        def recurse_with_memo(p1: int, p2: int):

            # last condition is an extra filter to exit recursion more quickly
            if p1 == s_len or p2 == t_len or s_len - p1 < t_len - p2:
                return int(p2 == t_len)

            if (p1, p2) in memo:
                return memo[(p1, p2)]

            ans = recurse_with_memo(p1 + 1, p2)

            if s[p1] == t[p2]:
                ans += recurse_with_memo(p1 + 1, p2 + 1)
            memo[(p1, p2)] = ans
            return ans

        memo = {}
        return recurse_with_memo(0, 0)
