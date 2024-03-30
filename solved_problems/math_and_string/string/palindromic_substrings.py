class PalindromicSubstrings:

    def countTotalV1(self, s: str) -> int:
        """
        Approach: Expand Centers
        T: O(N^2)
        S: O(1)
        :param s:
        :return:
        """
        if not s or len(s) == 1:
            return len(s)
        length = len(s)
        totalPalindromes = 0

        def expandCenters(left: int, right: int) -> int:
            total = 0
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1
                right += 1
                total += 1
            return total

        for index in range(length):
            totalPalindromes += expandCenters(index, index)
            totalPalindromes += expandCenters(index, index + 1)
        return totalPalindromes

    def countTotalV0(self, s: str) -> int:
        """
        Approach: DP
        S: O(N^2)
        T: O(N^2)
        :param s:
        :return:
        """
        if not s or len(s) == 1:
            return len(s)
        length = len(s)
        totalPalindromes = 0

        dp = [[False] * length for _ in range(length)]

        # single length odd palindrome marking
        for index in range(length):
            dp[index][index] = True
            totalPalindromes += 1

        # double length even palindrome marking
        for index in range(length - 1):
            if s[index] == s[index + 1]:
                dp[index][index + 1] = True
                totalPalindromes += 1

        currLength = 3

        while currLength <= length:
            left = 0
            while left < length - currLength + 1:
                right = left + currLength - 1
                if s[left] == s[right] and dp[left + 1][right - 1]:
                    dp[left][right] = True
                    totalPalindromes += 1
                left += 1
            currLength += 1
        return totalPalindromes


if __name__ == "__main__":
    pal = PalindromicSubstrings()
    print(pal.countTotalV0("abc"))
    print(pal.countTotalV0("aac"))
    print(pal.countTotalV0("aaa"))
    print("**__**")
    print(pal.countTotalV1("abc"))
    print(pal.countTotalV1("aac"))
    print(pal.countTotalV1("aaa"))
