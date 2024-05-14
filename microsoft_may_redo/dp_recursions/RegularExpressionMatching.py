class RegularExpression:

    def is_match_v1(self, s: str, p: str) -> bool:
        """
        Approach: DP Tabulation
        T: O(MN)
        S: O(MN)
        :param s:
        :param p:
        :return:
        """

        s_len = len(s)
        p_len = len(p)

        dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]
        dp[-1][-1] = True

        for p1 in range(s_len - 1, -1, -1):
            for p2 in range(p_len - 1, -1, -1):

                first_match = p1 < s_len and p[p1] in {'.', s[p1]}
                if p2 + 1 < p_len and p[p2 + 1] == '*':
                    dp[p1][p2] = dp[p1][p2 + 2] or first_match and dp[p1 + 1][p2]
                else:
                    dp[p1][p2] = first_match and dp[p1 + 1][p2 + 1]
        return dp[0][0]

    def is_match_v0(self, s: str, p: str) -> bool:
        """
        Approach: Recursion with memo
        T: O(MN)
        S: O(MN)
        :param s:
        :param p:
        :return:
        """

        def helper(p1: int, p2: int) -> bool:

            if (p1, p2) not in memo:

                if p2 == len(p):
                    ans = p1 == len(s)
                else:

                    first_match = p1 < len(s) and p[p2] in {'.', s[p1]}

                    if p2 + 1 < len(p) and p[p2 + 1] == '*':
                        ans = helper(p1, p2 + 2) or first_match and helper(p1, p2 + 1)
                    else:
                        ans = first_match and helper(p1 + 1, p2 + 1)
                memo[(p1, p2)] = ans
            return memo[(p1, p2)]

        memo = {}
        return helper(0, 0)
