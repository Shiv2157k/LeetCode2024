from typing import List
from collections import deque


class TrieNode:

    def __init__(self):
        self.isWord = False
        self.children = {}


class WordBreak:

    def isValidV2(self, s: str, wordDict: List[List[int]]) -> bool:
        """
        Approach: Trie
        T: O(n ^ 2 + m * K)
        S: O(n + m * K)
        :param s:
        :param wordDict:
        :return:
        """
        root = TrieNode()

        for word in wordDict:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.isWord = True

        dp = [False] * len(s)

        for left in range(len(s)):

            if left == 0 or dp[left - 1]:
                curr = root

                for right in range(left, len(s)):
                    char = s[right]
                    if char not in curr.children:
                        break
                    curr = curr.children[char]
                    if curr.isWord:
                        dp[right] = True
        return dp[-1]

    def isValidV2(self, s: str, wordDict: List[List[int]]) -> bool:
        """
        Approach: Bottom Up
        T: O(n * m * k)
        S: O(n)
        :param s:
        :param wordDict:
        :return:
        """

        dp = [False] * len(s)

        for index in range(len(s)):
            for word in wordDict:
                if index < len(word) - 1:
                    continue
                if index == len(word) - 1 or dp[index - len(word)]:
                    if s[index - len(word) + 1: index + 1] == word:
                        dp[index] = True
                        break
        return dp[-1]

    def isValidV1(self, s: str, wordDict: List[List[int]]) -> bool:
        """
        Approach: Top Down
        T: O(n * m * k)
        S: O(n)
        :param s:
        :param wordDict:
        :return:
        """
        memo = [-1] * len(s)

        def recurseWithMemo(ptr: int):

            if ptr < 0:
                return True
            if memo[ptr] != -1:
                return memo[ptr] == 1

            for word in wordDict:
                if ptr - len(word) + 1 >= 0:
                    if s[ptr - len(word) + 1: ptr + 1] == word and recurseWithMemo(ptr - len(word)):
                        memo[ptr] = 1
                        return True
            memo[ptr] = 0
            return False

    def isValidV0(self, s: str, wordDict: List[List[int]]) -> bool:
        """
        Approach: Queue
        T: O(N ^ 3 + M * K)
        S: O(N + M * K)
        :param s:
        :param wordDict:
        :return:
        """

        wordSet = set(wordDict)

        visited = set()

        queue = deque([0])

        while queue:

            left = queue.popleft()
            if left == len(s):
                return True
            for right in range(left + 1, len(s) + 1):
                if right not in visited:
                    if s[left: right] in wordSet:
                        queue.append(right)
                        visited.add(right)
        return False
