from typing import List


class WordBreak:

    def is_word_break_v1(self, s: str, word_list: List[str]) -> bool:
        """
        DP Tabulation
        T: O(n.m.k)
        S: O(n)
        :param s:
        :param word_list:
        :return:
        """

        dp = [False] * len(s)

        for i in range(len(s)):

            for word in word_list:

                if i - len(word) <= 0:
                    continue

                if i == len(word) - 1 or dp[i - len(word)]:
                    if s[i - len(word) + 1: i + 1] == word:
                        dp[i] = True
                        break
        return dp[-1]

    def is_word_break_v0(self, s: str, word_list: List[str]) -> bool:
        """
        Approach: DP Memoization
        T: O(n.m.k)
        S:O(n)
        :param s:
        :param word_list:
        :return:
        """

        def helper(pos: int) -> bool:

            if pos <= 0:
                return True
            if memo[pos] != -1:
                return memo[pos] == 1
            # leetcode -> 8 - 4
            for word in word_list:

                if pos - len(word) + 1 >= 0:
                    if s[pos - len(word) + 1: pos + 1] == word and helper(pos - len(word)):
                        memo[pos] = 1
                        return True
            memo[pos] = 0
            return False

        memo = [-1] * len(s)
        return helper(len(s) - 1)
