class Palindrome:

    def longestPalindromicSubstringV1(self, s: str) -> str:
        """
        Approach: Expand Centers
        T: O(N ^ 2)
        S: O(1)
        :param s:
        :return:
        """
        if not s or len(s) == 1:
            return s
        length = len(s)
        ans = [0, 0]

        def expandCenter(left: int, right: int) -> int:
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        for index in range(length):

            oddLength = expandCenter(index, index)
            if oddLength > ans[1] - ans[0] + 1:
                mid = oddLength // 2
                ans = [index - mid, index + mid]

            evenLength = expandCenter(index, index + 1)
            if evenLength > ans[1] - ans[0] + 1:
                mid = (evenLength - 1) // 2
                ans = [index - mid, index + mid + 1]
        return s[ans[0]: ans[1] + 1]

    def longestPalindromicSubstringV0(self, s: str) -> str:
        """
        Approach: DP
        T: O(N^2)
        S: O(N^2)
        :param s:
        :return:
        """

        if not s or len(s) == 1:
            return s

        length = len(s)

        dp = [[False] * length for _ in range(length)]

        maxLen = 1
        start = 1

        # mark the single len odd palindrome
        for index in range(length):
            dp[index][index] = True

        # mark the double length even palindrome
        for index in range(length - 1):
            if s[index] == s[index + 1]:
                dp[index][index + 1] = True
                maxLen = 2
                start = index

        currLen = 3
        while currLen <= length:

            left = 0

            while left < length - currLen + 1:
                right = currLen - 1 + left

                if s[left] == s[right] and dp[left + 1][right - 1]:
                    dp[left][right] = True
                    if maxLen < currLen:
                        maxLen = currLen
                        start = left
                left += 1
            currLen += 1
        return s[: start] if start == maxLen else s[start: start + maxLen]


if __name__ == "__main__":
    pal = Palindrome()
    print(pal.longestPalindromicSubstringV0("babad"))
    print(pal.longestPalindromicSubstringV0("cbbd"))

    print(pal.longestPalindromicSubstringV1("babad"))
    print(pal.longestPalindromicSubstringV1("cbbd"))

