class RegularExpression:

    def isMatchV1(self, s: str, p: str) -> bool:
        """
        Approach: Top Down DP
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

                firstMatch = row < len(s) and p[col] in {".", s[row]}

                if col + 1 < len(p) and p[col + 1] == "*":
                    dp[row][col] = dp[row][col + 2] or firstMatch and dp[row + 1][col]
                else:
                    dp[row][col] = firstMatch and dp[row + 1][col + 1]
        return dp[0][0]

    def isMatchV0(self, s: str, p: str) -> bool:
        """
        Approach: Bottom Up DP
        T: O(TP)
        S: O(TP)
        :param s:
        :param p:
        :return:
        """

        if not p:
            return not s

        memo = {}

        def recurse_with_memo(sPtr, pPtr) -> bool:
            if (sPtr, pPtr) not in memo:
                # base case if p reached to end
                if pPtr == len(p):
                    ans = sPtr == len(s)
                else:
                    firstMatch = sPtr < len(s) and p[pPtr] in {".", s[sPtr]}

                    # case 1: "*"
                    if pPtr + 1 < len(p) and p[pPtr + 1] == "*":
                        ans = recurse_with_memo(sPtr, pPtr + 2) or firstMatch and recurse_with_memo(sPtr + 1, pPtr)
                    # case 2: "." or a match
                    else:
                        ans = recurse_with_memo(sPtr + 1, pPtr + 1)

                memo[sPtr, pPtr] = ans
            return memo[sPtr, pPtr]

        return recurse_with_memo(0, 0)


if __name__ == "__main__":
    regularExpression = RegularExpression()
    print(regularExpression.isMatchV0("aa", "a*"))
    print(regularExpression.isMatchV1("aa", "a*"))

    print(regularExpression.isMatchV0("aa", ".a"))
    print(regularExpression.isMatchV1("aa", ".a"))

    print(regularExpression.isMatchV0("aa", "a"))
    print(regularExpression.isMatchV1("aa", "a"))

    print(regularExpression.isMatchV0("abaab", "a..a*"))
    print(regularExpression.isMatchV1("abaab", "a..a*"))

    print(regularExpression.isMatchV0("abaab", "a..a*."))
    print(regularExpression.isMatchV1("abaab", "a..a*."))
