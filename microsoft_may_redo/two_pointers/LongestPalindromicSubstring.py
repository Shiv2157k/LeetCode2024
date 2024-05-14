class LongestPalindromicSubstring:

    def longest_palindrome(self, s: str) -> str:
        """
        Approach: Expand Center
        T: O(N^2)
        S: O(1)
        :param s:
        :return:
        """

        ans = [0, 0]

        for i in range(len(s)):
            odd_len = self.__expand_center(s, i, i)
            if odd_len > ans[1] - ans[0] + 1:
                mid_len = odd_len // 2
                ans = [i - mid_len, i + mid_len]

            even_len = self.__expand_center(s, i, i + 1)
            if even_len > ans[1] - ans[0] + 1:
                mid_len = (even_len - 1) // 2
                ans = [i - mid_len, i + mid_len + 1]

        return s[ans[0]: ans[1] + 1]

    def __expand_center(self, s: str, left: int, right: int) -> int:
        """
        :param s:
        :param left:
        :param right:
        :return:
        """

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left += 1
            right -= 1
        return right - left - 1
