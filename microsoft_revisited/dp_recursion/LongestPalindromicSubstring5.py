class LongestPalindromicSubstrings:

    def getLongestSubstringsV1(self, s: str) -> str:
        """
        Approach: Expand Center
        ToDo: Note: Manacher's Algorithm - O(N)
        T: O(N^2)
        S: O(1)
        :param s:
        :return:
        """
        if not s:
            return ''

        boundary = [0, 0]

        def expandCenter(left: int, right: int):

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        for index in range(len(s)):

            oddLen = expandCenter(index, index)
            # expand boundaries
            if oddLen > boundary[1] - boundary[0] + 1:
                mid = oddLen // 2
                # new boundary
                boundary = [index - mid, index + mid]

            evenLen = expandCenter(index, index + 1)
            # expand boundaries
            if evenLen > boundary[1] - boundary[0] + 1:
                mid = (evenLen - 1) // 2
                boundary = [index - mid, index + mid + 1]

        return s[boundary[0]: boundary[1] + 1]

    def getLongestSubstringsV0(self, s: str) -> str:
        """
        Approach: DP
        T: O(N^2)
        S: O(N^2)
        :param s:
        :return:
        """

        dp = [[False] * len(s) for _ in range(len(s))]
        start, maxLen = 1, 1

        # oddLen
        for row in range(len(s)):
            dp[row][row] = True

        # even length
        for row in range(len(s) - 1):
            if s[row] == s[row + 1]:
                dp[row][row + 1] = True
                start = row
                maxLen = 2

        currLen = 3

        while currLen <= len(s):
            left = 0
            while left < len(s) - currLen + 1:
                right = currLen - 1 + left

                if s[left] == s[right] and dp[left + 1][right - 1]:
                    dp[left][right] = True
                    if maxLen < currLen:
                        maxLen = dp[left][right]
                        start = left
                left += 1
            currLen += 1
        return s[:start] if maxLen == start else s[start: maxLen + start]
