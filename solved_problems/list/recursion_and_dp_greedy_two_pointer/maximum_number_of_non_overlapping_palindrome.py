class NonOverlappingPalindrome:

    def max_number(self, s: str, k: int) -> int:
        """
        Approach: DP
        T: O(NK)
        S: O(N)
        :param s:
        :param k:
        :return:
        """
        n = len(s)
        dp = [0] * (n + 1)

        for index in range(k, n + 1):
            dp[index] = dp[index - 1]
            if self._is_palindrome(s, index - k, index - 1):
                dp[index] = max(dp[index], 1 + dp[index - k])
            if index - k - 1 >= 0:
                if self._is_palindrome(s, index - k - 1, index - 1):
                    dp[index] = max(dp[index], 1 + dp[index - k - 1])
        return dp[n]

    def _is_palindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    string = NonOverlappingPalindrome()
    print(string.max_number("abaccdbbbd", 3))
    print(string.max_number("abaccdbbbd", 2))
