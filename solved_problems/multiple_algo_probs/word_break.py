from collections import deque
from typing import List


class TrieNode:

    def __init__(self):
        self.is_word_end = False
        self.children = {}


class WordBreak:
    """
    This problem consists of below algorithms:
    1. BFS
    2. DP Variations - 2
    3. Trie
    """

    def is_valid_v1(self, s: str, word_list: List[str]) -> bool:
        """
        i/p: s: "leetcode", word_list = ["leet", "code"], o/p: true
        i/p: s: "applepenapple", word_list = ["apple","pen"], o/p: true
        i/p: s: "catsandog", word_list = ["cats","dog","sand","and","cat"], o/p: false
        TC: O((n3+m⋅k))
        SC: O(n + m * k)
        :param s:
        :param word_list:
        :return:
        """
        # idea is to check words starting from i -> i + word, i + word len -> i + word1len ---
        # convert wordlist to set to eliminate duplicates
        word_set = set(word_list)
        # to track already visited
        visited = set()
        # for traversing
        queue = deque()
        queue.append(0)

        while queue:
            left = queue.popleft()
            if left == len(s):
                return True
            for right in range(left + 1, len(s) + 1):
                if right not in visited:
                    if s[left: right] in word_set:
                        queue.append(right)
                        visited.add(right)
        return False

    def is_valid_v2(self, s: str, word_list: List[str]) -> bool:
        """
        Approach: Top Down DP - Memoization
        :param s:
        :param word_list:
        :return:
        """
        memo = [-1] * len(s)

        def topdown(index: int):
            # base case
            if index < 0:
                return True
            if memo[index] != -1:
                return memo[index] == 1

            for word in word_list:
                if index - len(word) + 1 >= 0:
                    if s[index - len(word) + 1: index + 1] == word and topdown(index - len(word)):
                        memo[index] = 1
                        return True
            memo[index] = 0
            return False

        return topdown(len(s) - 1)

    def is_valid_v3(self, s: str, word_list: List[str]) -> bool:
        """
        DP: Bottom Up
        :param s:
        :param word_list:
        :return:
        """
        dp = [False] * len(s)

        for index in range(len(s)):
            for word in word_list:
                if index < len(word) - 1:
                    continue
                if index == len(word) - 1 or dp[index - len(word)]:
                    if s[index - len(word) + 1: index + 1] == word:
                        dp[index] = True
        return dp[-1]

    def is_valid_v4(self, s: str, word_list: List[str]) -> bool:
        """
        Approach: Trie
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
            curr.is_word_end = True

        dp = [False] * len(s)

        for left in range(len(s)):
            if left == 0 or dp[left - 1]:
                curr = root
                for right in range(left, len(s)):
                    char = s[right]
                    if char not in curr.children:
                        break
                    curr = curr.children[char]
                    if curr.is_word_end:
                        dp[right] = True
        return dp[-1]

    def is_valid_v5(self, s: str, word_list: List[str]) -> bool:
        """
        Approach: DP
        :param s:
        :param word_list:
        :return:
        """
        word_set = set(word_list)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for left in range(len(s) + 1):
            for right in range(left + 1, len(s) + 1):
                if dp[left] and s[left: right] in word_set:
                    dp[right] = True
                    break
        return dp[-1]




if __name__ == "__main__":
    word_break = WordBreak()
    print(word_break.is_valid_v1(
        "leetcode",  ["leet", "code"]
    ))
    print(word_break.is_valid_v1(
        "applepenapple",["apple","pen"]
    ))
    print(word_break.is_valid_v1(
    "catsandog",["cats","dog","sand","and","cat"]
    ))
    print("___*___")
    print(word_break.is_valid_v2(
        "leetcode", ["leet", "code"]
    ))
    print(word_break.is_valid_v2(
        "applepenapple", ["apple", "pen"]
    ))
    print(word_break.is_valid_v2(
        "catsandog", ["cats", "dog", "sand", "and", "cat"]
    ))
    print("___*___")
    print(word_break.is_valid_v3(
        "leetcode", ["leet", "code"]
    ))
    print(word_break.is_valid_v3(
        "applepenapple", ["apple", "pen"]
    ))
    print(word_break.is_valid_v3(
        "catsandog", ["cats", "dog", "sand", "and", "cat"]
    ))
    print("___*___")
    print(word_break.is_valid_v4(
        "leetcode", ["leet", "code"]
    ))
    print(word_break.is_valid_v4(
        "applepenapple", ["apple", "pen"]
    ))
    print(word_break.is_valid_v4(
        "catsandog", ["cats", "dog", "sand", "and", "cat"]
    ))
    print("___*___")
    print(word_break.is_valid_v5(
        "leetcode", ["leet", "code"]
    ))
    print(word_break.is_valid_v5(
        "applepenapple", ["apple", "pen"]
    ))
    print(word_break.is_valid_v5(
        "catsandog", ["cats", "dog", "sand", "and", "cat"]
    ))
    print("___*___")
