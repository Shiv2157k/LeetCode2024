class LongestPalindromicSubstring:

    def longest_palindrome(self, s: str) -> str:
        """
        Approach: DP
        T: O(N^2)
        S: O(N^2)
        :param s:
        :return:
        """

        length = len(s)

        dp = [[False] * length for _ in range(length)]

        start = 0
        max_len = 1

        # odd len palindrome
        for row in range(length):
            dp[row][row] = True

        # even len palindrome:
        for row in range(length - 1):
            if s[row] == s[row + 1]:
                dp[row][row + 1] = True
                start = row
                max_len = 2

        curr_len = 3

        while curr_len <= length:

            left = 0

            while left < length - curr_len + 1:
                right = curr_len - 1 + left

                if s[left] == s[right] and dp[left - 1][right + 1]:
                    dp[left][right] = True
                    if max_len < curr_len:
                        max_len = curr_len
                        start = left
                left += 1
            curr_len += 1
        return s[:start] if max_len == start else s[start: start + max_len]
