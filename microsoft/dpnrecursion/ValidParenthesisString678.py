from typing import List


class ValidParenthesisString:

    def checkValidityV1(self, s: str) -> bool:
        """
        Approach: Tabulation
        T: O(N * N)
        S: O(N * N)
        :param s:
        :return:
        """

        n = len(s)

        dp = [[False] * (n + 1) for _ in range(n + 1)]

        # base case for empty string
        dp[n][0] = True

        for index in range(n - 1, -1, -1):
            for openBracket in range(n):

                isValid = False

                if s[index] == "*":

                    if openBracket < n:
                        # try "*" -> "("
                        isValid |= dp[index + 1][openBracket + 1]

                    if openBracket > 0:
                        # try "*" -> ")"
                        isValid |= dp[index + 1][openBracket - 1]
                    # ignore "*" as an empty string
                    isValid |= dp[index + 1][openBracket]
                else:
                    if s[index] == "(":
                        isValid |= dp[index + 1][openBracket + 1]
                    elif openBracket > 0:
                        isValid |= dp[index + 1][openBracket - 1]
                dp[index][openBracket] = isValid
        return dp[0][0]

    def checkValidityV0(self, s: str) -> bool:
        """
        Approach: DP Memoization
        T: O(N * N)
        S: O(N * N)
        :param s:
        :return:
        """

        n = len(s)
        memo = [[-1] * n for _ in range(n)]
        return self.isValidString(0, 0, s, memo)

    def isValidString(self, ptr: int, openCount: int, s: str, memo: List[List[str]]) -> bool:

        # base case
        if len(s) == ptr:
            return openCount == 0
        if memo[ptr][openCount] != -1:
            return memo[ptr][openCount] == 1

        isValid = False

        if s[ptr] == '*':
            # considering an extra close bracket
            isValid |= self.isValidString(ptr + 1, openCount + 1, s, memo)

            # considering an extra open bracket
            if openCount > 0:
                isValid |= self.isValidString(ptr + 1, openCount - 1, s, memo)
            # considering it as an empty string
            isValid |= self.isValidString(ptr + 1, openCount, s, memo)

        else:
            if s[ptr] == '(':
                isValid = self.isValidString(ptr + 1, openCount + 1, s, memo)
            elif openCount > 0:
                isValid = self.isValidString(ptr + 1, openCount - 1, s, memo)
        memo[ptr][openCount] = 1 if isValid else 0
        return isValid
