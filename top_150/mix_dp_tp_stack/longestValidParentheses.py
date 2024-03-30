class Parentheses:

    def longestValidLengthV3(self, s: str) -> int:
        """
        Approach: Two Pointer
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """

        left, right, maxLen = 0, 0, 0

        for index in range(len(s)):

            if s[index] == "(":
                left += 1
            else:
                right += 1

            if left == right:
                maxLen = max(maxLen, left * 2)
            elif right > left:
                left = 0
                right = 0

        left, right = 0, 0

        for index in range(len(s) - 1, -1, -1):

            if s[index] == "(":
                left += 1
            else:
                right += 1

            if left == right:
                maxLen = max(maxLen, right * 2)
            elif left > right:
                left = 0
                right = 0
        return maxLen

    def longestValidLengthV2(self, s: str) -> int:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """

        stack = [-1]
        maxLen = 0

        for index, char in enumerate(s):
            if char == "(":
                stack.append(index)
            else:
                stack.pop()
                if not stack:
                    stack.append(index)
                else:
                    maxLen = max(maxLen, index - stack[-1])
        return maxLen

    def longestValidLengthV1(self, s: str) -> int:
        """
        Approach: DP
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """

        maxLen = 0

        dp = [0] * len(s)

        for index in range(1, len(s)):

            if s[index] == ")":

                if s[index - 1] == "(":
                    dp[index] = dp[index - 2] + 2
                elif index - dp[index - 1] > 0 and s[index - dp[index - 1] - 1] == "(":
                    dp[index] = dp[index - 1] + dp[index - dp[index - 1] - 2] + 2
                maxLen = max(maxLen, dp[index])
        return maxLen

    def longestValidLengthV0(self, s: str) -> int:
        """
        Approach: BRute Force
        T: O(N ^ 3)
        S: O(N)
        :param s:
        :return:
        """

        def isValid(subString: str) -> bool:
            stack = []
            for char in subString:
                if char == "(":
                    stack.append(char)
                elif stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            return not stack

        maxLen = 0
        for i in range(len(s)):
            for j in range(i + 2, len(s), 2):
                if isValid(s[i: j]):
                    maxLen = max(maxLen, j - i)
        return maxLen


if __name__ == "__main__":
    parentheses = Parentheses()
    print(parentheses.longestValidLengthV0(")()())"))
    print(parentheses.longestValidLengthV1(")()())"))
    print(parentheses.longestValidLengthV2(")()())"))
    print(parentheses.longestValidLengthV3(")()())"))
