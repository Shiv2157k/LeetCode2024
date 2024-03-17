

class Parenthesis:

    def longest_valid_parantheses_v3(self, s: str) -> int:
        """
        Approach: Two Pointer Space Optimization
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """
        left = right = max_len = 0
        for index in range(len(s)):
            if s[index] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                max_len = max(max_len, right * 2)
            elif right > left:
                left = right = 0
        left = right = 0
        for index in range(len(s) - 1, -1, -1):
            if s[index] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                max_len = max(max_len, left * 2)
            elif left > right:
                left = right = 0
        return max_len


    def longest_valid_parantheses_v2(self, s: str) -> int:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """
        stack = [-1]
        max_len = 0
        for index, char in enumerate(s):
            if char == "(":
                stack.append(index)
            else:
                stack.pop()
                if not stack:
                    stack.append(index)
                else:
                    max_len = max(max_len, index - stack[-1])
        return max_len

    def longest_valid_parantheses_v1(self, s: str) -> int:
        """
        Approach: DP
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """
        dp = [0] * len(s)
        max_len = 0
        for index in range(1, len(s)):
            if s[index] == ")":
                # case1: if s[i - 1] = "(", s[i] = ")"
                if s[index - 1] == "(":
                    dp[index] = dp[index - 2] + 2
                # case 2: if s[i - 1] = ")", s[i] = ")"
                elif index - dp[index - 1]  > 0 and s[index - dp[index - 1] - 1] == "(":
                    dp[index] = dp[index - 1] + dp[index - dp[index - 1] - 2] + 2
                max_len = max(max_len, dp[index])
        return max_len

    def longest_valid_parantheses_v0(self, s: str) -> int:
        """
        Brute Force
        T: O(N^3)
        S: O(1)
        :param s:
        :return:
        """
        def is_valid(prefix: str) -> bool:
            """
            ()()) -> False
            (())) -> False
            :param prefix:
            :return:
            """
            stack = []
            for char in prefix:
                if char == "(":
                    stack.append(char)
                elif stack and stack[-1] == "(":
                    stack.pop()
            return not stack
        max_len = 0
        for left in range(len(s)):
            for right in range(left + 2, len(s) + 1, 2):
                if is_valid(s[left: right]):
                    max_len = max(max_len, right - left)
        return max_len

