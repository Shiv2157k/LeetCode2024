from typing import List
from collections import defaultdict


class WordBreakII:

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        memo = defaultdict(list)
        wordSet = set(wordDict)

        def helper(s: str):

            if not s:
                return [[]]
            if s in memo:
                return memo[s]

            for i in range(1, len(s) + 1):
                if s[: i] in wordSet:

                    for subSeq in helper(s[i:]):
                        memo[s].append([s[:i]] + subSeq)
            return memo[s]

        helper(s)
        result = []

        for word in memo[s]:
            result.append(''.join(word))
        return result
