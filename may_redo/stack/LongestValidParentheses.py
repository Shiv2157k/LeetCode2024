from typing import List


class LongestValidParentheses:

    def longest_valid_parentheses(self, s: str) -> int:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """

        stack = [-1]
        max_len = 0

        for i, char in enumerate(s):

            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len
