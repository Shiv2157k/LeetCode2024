from collections import deque
from typing import List


class Trie:

    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordBreak:

    def canWordBreakV3(self, s: str, wordDict: List[str]) -> bool:
        """
        Approach: DP with Trie
        T: O(N^2 + M * K)
        S: O(N = M + K)
        :param s:
        :param wordDict:
        :return:
        """

        root = Trie()

        for word in wordDict:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = Trie()
                curr = curr.children[char]
            curr.isEnd = True

        dp = [False] * len(s)
        for left in range(len(s)):
            if left == 0 or dp[left - 1]:
                curr = root
                for right in range(left, len(s)):
                    char = s[right]
                    if char not in curr.children:
                        break
                    curr = curr.children[char]
                    if curr.isEnd:
                        dp[right] = True
        return dp[-1]

    def canWordBreakV2(self, s: str, wordDict: List[str]) -> bool:
        """
        Approach: DP
        T: O(N * M * K)
        S: O(N)
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

    def canWordBreakV1(self, s: str, wordDict: List[str]) -> bool:
        """
        Approach: Recurse with Memo
        T: O(N * M * K)
        S: O(N)
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

        return recurseWithMemo(len(s) - 1)

    def canWordBreakV0(self, s: str, wordDict: List[str]) -> bool:
        """
        Approach: BFS
        T: O(n^3 + m.k)
        S: O(n + m * k)
        :param s:
        :param wordDict:
        :return:
        """
        wordSet = set(wordDict)
        visited = set()

        queue = deque()
        queue.append(0)

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
