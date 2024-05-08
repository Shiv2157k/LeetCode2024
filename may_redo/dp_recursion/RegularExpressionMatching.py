class RegularExpressionMatching:

    def is_match_v2(self, s: str, p: str) -> bool:
        """
        Approach: DP with Tabulation
        T: O(N * M)
        S: O(N * M)
        :param s:
        :param p:
        :return:
        """

        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[-1][-1] = True

        for row in range(len(s), - 1, -1):
            for col in range(len(p) - 1, -1, -1):
                first_match = row < len(s) and p[col] in {s[row], '.'}
                if col + 1 < len(p) and p[col + 1] == '*':
                    dp[row][col] = dp[row][col + 2] or first_match and dp[row + 1][col]
                else:
                    dp[row][col] = first_match and dp[row + 1][col + 1]
        return dp[0][0]

    def is_match_v1(self, s: str, p: str) -> bool:
        """
        Approach: Recursion with memoization
        T: O(N*M)
        S: O(N * M)
        :param s:
        :param p:
        :return:
        """

        memo = {}

        def helper(p1: int, p2: int) -> bool:

            if (p1, p2) not in memo:

                if p2 == len(p):
                    ans = p1 == len(s)
                else:
                    first_match = p1 < len(s) and p[p2] in {'.', s[p1]}

                    if p2 + 1 < len(p) and p[p2 + 1] == '*':
                        ans = helper(p1, p2 + 2) or first_match and helper(p1 + 1, p2)
                    else:
                        ans = first_match and helper(p1 + 1, p2 + 1)
                memo[(p1, p2)] = ans
            return memo[(p1, p2)]

        return helper(0, 0)

    def is_match_v0(self, s: str, p: str) -> bool:
        """
        Approach: Recursion
        T: O((T + P) ^ (2^ (T + P / 2)))
        S: O((T + P) * (2^(T + P / 2)))
        :param s:
        :param p:
        :return:
        """

        if not p:
            return not s
        # pattern[0] == text[0] -> p = a*, t = aab -> [a]* == [a]ab
        # pattern[0] == . -> p = '.a', t = 'ca' -> [.]a == [c]a
        first_match = s and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':
            # case 1: pattern = a*.b, text= cb
            # case 2:
            # - pattern = c*b, text=cb
            # - pattern = .*b, text= cb
            return self.is_match_v0(s, p[2:]) or first_match and self.is_match_v0(s[1:], p)
        else:
            return first_match and self.is_match_v0(s[1:], p[1:])
