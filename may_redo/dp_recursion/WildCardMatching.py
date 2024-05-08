class WildCardMatching:

    def is_match_v2(self, s: str, p: str) -> bool:
        """
        Approach: BackTrack with four pointers
        T: O(SP)
        S: O(1)
        :param s:
        :param p:
        :return:
        """

        s_len, p_len = len(s), len(p)
        s_ptr, p_ptr = 0, 0
        start_ptr = -1
        temp_ptr = -1

        while s_ptr < s_len:
            # If the pattern character = string character
            # or pattern character = '?'
            if p_ptr < p_len and p[p_ptr] in {'?', s[s_ptr]}:
                p_ptr += 1
                s_ptr += 1
            # If pattern character = '*'
            elif p_ptr < p_len and p[p_ptr] == '*':
                # Check the situation
                # when '*' matches no characters
                start_ptr = p_ptr
                temp_ptr = s_ptr
                p_ptr += 1
            # If pattern character != string character
            # or pattern is used up
            # and there was no '*' character in pattern
            elif start_ptr == -1:
                return False
            # If pattern character != string character
            # or pattern is used up
            # and there was '*' character in pattern before
            else:
                # Backtrack: check the situation
                # when '*' matches one more character
                p_ptr = start_ptr + 1
                s_ptr = temp_ptr + 1
                temp_ptr = s_ptr

        while p_ptr < p_len:
            if p[p_ptr] != '*':
                return False
            p_ptr += 1
        return True

    def is_match_v1(self, s: str, p: str) -> bool:
        """
        Approach: DP Tabulation
        T: O(MN)
        S: O(MN)
        :param s:
        :param p:
        :return:
        """

        def remove_duplicate_stars(p: str) -> str:
            refined_pattern = []
            for char in p:

                if not refined_pattern or char != '*':
                    refined_pattern.append(char)
                elif refined_pattern[-1] != '*':
                    refined_pattern.append(char)
            return ''.join(refined_pattern)

        p = remove_duplicate_stars(p)

        if s == p or p == '*':
            return True
        if s == '' or p == '*':
            return False

        s_len = len(s)
        p_len = len(p)

        dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]
        dp[0][0] = True

        for p2 in range(1, p_len + 1):
            if p[p2 - 1] != '*':
                break
            dp[0][p2] = True

        for p1 in range(1, s_len + 1):
            for p2 in range(1, p_len + 1):

                if p[p2 - 1] == '?' or p[p2 - 1] == s[p1 - 1]:
                    dp[p1][p2] = dp[p1 - 1][p2 - 1]
                elif p[p2 - 1] == '*':
                    dp[p1][p2] = dp[p1 - 1][p2] or dp[p1][p2 - 1]
        return dp[-1][-1]

    def is_match_v0(self, s: str, p: str) -> bool:
        """
        Approach: Recurse with memo
        T: O(S * P * (S + P))
        S: O(S * P)
        :param s:
        :param p:
        :return:
        """

        def remove_duplicate_stars(p: str) -> str:
            refined_pattern = []
            for char in p:

                if not refined_pattern or char != '*':
                    refined_pattern.append(char)
                elif refined_pattern[-1] != '*':
                    refined_pattern.append(char)
            return ''.join(refined_pattern)

        def memo_solve(s: str, p: str) -> bool:
            # cases
            # p[i] in {'?', s[i]}:
            # i > 1 and p[i] == '*' two cases consider s[i] or not consider s[i]
            if (s, p) in memo:
                return memo[(s, p)]

            if p == s or p == '*':
                memo[(s, p)] = True
            elif p == '' or s == '':
                memo[(s, p)] = False
            elif p[0] == s[0] or p[0] == '?':
                memo[(s, p)] = memo_solve(s[1:], p[1:])
            elif p[0] == '*':
                memo[(s, p)] = memo_solve(s[1:], p) or memo_solve(s, p[1:])
            else:
                memo[(s, p)] = False
            return memo[(s, p)]

        memo = {}
        p = remove_duplicate_stars(p)
        return memo_solve(s, p)
