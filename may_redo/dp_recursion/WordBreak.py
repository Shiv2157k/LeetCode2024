from typing import List


class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False


class WordBreak:

    def word_break_v0(self, s: str, wordDict: List[str]) -> bool:
        """
        Approach: Recurse with memo
        T: O(n * m * k)
        S: O(n)
        :param s:
        :param wordDict:
        :return:
        """

        def recurse_with_memo(ptr: int) -> bool:

            if ptr < 0:
                return True

            if memo[ptr] != -1:
                return memo[ptr] == 1

            for word in wordDict:
                if ptr - len(word) + 1 >= 0:
                    if s[ptr - len(word) + 1: ptr + 1] == word and recurse_with_memo(ptr - len(word)):
                        memo[ptr] = 1
                        return True
            memo[ptr] = 0
            return False

        memo = [-1] * len(s)
        return recurse_with_memo(len(s) - 1)

    def word_break_v1(self, s: str, wordDict: List[str]) -> bool:
        """
        Approach: DP
        T: O(N * M * k)
        S: O(N)
        :param s:
        :param wordDict:
        :return:
        """

        dp = [False] * len(s)

        for i in range(len(s)):

            for word in wordDict:

                if i < len(word) - 1:
                    continue

                if i == len(word) - 1 or dp[i - len(word)]:
                    if s[i - len(word) + 1: i + 1] == word:
                        dp[i] = True
                        break
        return dp[-1]

    def word_break_v2(self, s: str, wordDict: List[str]) -> bool:
        """
        Approach: DP and Trie
        T: O(n^2 + m * k)
        S: O(n + m * k)
        :param s:
        :param wordDict:
        :return:
        """

        root = TrieNode()

        for word in wordDict:
            curr = root
            for letter in word:
                curr.children[letter] = curr.children.get(letter, TrieNode())
                curr = curr.children[letter]
            curr.is_word = True

        dp = [False] * len(s)

        for left in range(len(s)):
            if left == 0 or dp[left - 1]:
                curr = root
                for right in range(left, len(s)):
                    char = s[right]
                    if char not in curr.children:
                        break
                    curr = curr.children[char]
                    if curr.is_word:
                        dp[right] = True
        return dp[-1]
