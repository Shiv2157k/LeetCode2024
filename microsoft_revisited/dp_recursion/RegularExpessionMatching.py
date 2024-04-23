class RegularExpression:

    def isMatchV1(self, s: str, p: str) -> bool:
        """
        Approach: DP Tabulation
        T: O(TP)
        S: O(TP)
        :param s:
        :param p:
        :return:
        """

        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[-1][-1] = True

        for row in range(len(s), -1, -1):
            for col in range(len(p) - 1, -1, -1):

                firstMatch = row < len(s) and p[col] in {'.', s[row]}

                if col + 1 < len(p) and p[col + 1] == '*':
                    dp[row][col] = dp[row][col + 2] or firstMatch and dp[row + 1][col]
                else:
                    dp[row][col] = firstMatch and dp[row + 1][col + 1]
        return dp[0][0]

    def isMatchV0(self, s: str, p: str) -> bool:
        """
        Approach: Recursion with memo
        T: O(TP)
        S: O(TP)
        :param s:
        :param p:
        :return:
        """
        # cases to consider
        # 1. s[i] == p[i] or p[i] == '.'
        # 2. len(p) >= 2 p[1] == '*'
        memo = {}

        def recurseWithMemo(si, pi):

            if (si, pi) not in memo:
                if pi == len(p):
                    ans = si == len(s)
                else:
                    firstMatch = si < len(s) and p[pi] in {s[si], '.'}

                    if pi + 1 > len(p) and p[pi + 1] == '*':
                        ans = recurseWithMemo(si, pi + 2) or firstMatch and recurseWithMemo(si + 1, pi)
                    else:
                        ans = firstMatch and recurseWithMemo(si + 1, pi + 1)
                memo[si, pi] = ans
            return memo[si, pi]

        return recurseWithMemo(0, 0)
