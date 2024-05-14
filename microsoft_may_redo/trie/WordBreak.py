from typing import List


class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False


class WordBreak:

    def is_word_break(self, s: str, word_list: List[str]) -> bool:
        """
        Approach: Trie
        T: O(n^2 + m . k)
        S: O(n + m * k)
        :param s:
        :param word_list:
        :return:
        """

        root = TrieNode()

        for word in word_list:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.is_word = True

        dp = [False] * len(s)

        for left in range(len(s)):
            if left == 0 or dp[left - 1]:
                curr = root
                for right in range(left, len(s)):
                    letter = s[right]

                    if letter not in curr.children:
                        break
                    curr = curr.children[letter]
                    if curr.is_word:
                        dp[right] = True
        return dp[-1]
