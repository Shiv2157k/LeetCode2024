from typing import List


class LongestValidParentheses:

    def longest_valid_parentheses(self, s: str) -> int:
        """
        Approach: Two Pointers
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """

        left, right = 0, 0
        max_len = 0

        # left -> right
        for index in range(len(s)):

            if s[index] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                max_len = max(max_len, left * 2)
            elif right > left:
                # reset
                left = 0
                right = 0

        # right -> left

        for index in range(len(s) - 1, -1, -1):

            if s[index] == '(':
                left += 1
            else:
                right -= 1

            if left == right:
                max_len = max(max_len, right * 2)
            elif left > right:
                left = 0
                right = 0
        return max_len
