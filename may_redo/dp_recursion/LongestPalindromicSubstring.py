class LongestPalindromicSubstring:

    def longest_palindrome(self, s: str) -> str:
        """
        Approach: DP
        T: O(N^2)
        S: O(N^2)
        :param s:
        :return:
        """

        if not s or len(s) == 1:
            return s

        dp = [[False] * len(s) for _ in range(len(s))]
        start = 0
        max_len = 1

        for i in range(len(s)):
            dp[i][i] = True

        for i in range(len(s) - 1):
            if s[i] == s[i - 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2

        curr_len = 3

        while curr_len <= len(s):

            left = 0
            while left < len(s) - curr_len + 1:
                right = curr_len + left - 1

                if s[left] == s[right] and dp[left + 1][right - 1]:
                    dp[left][right] = True
                    if max_len < curr_len:
                        max_len = curr_len
                        start = left
                left += 1
            curr_len += 1
        return s[:start] if max_len == start else s[start: start + max_len]
