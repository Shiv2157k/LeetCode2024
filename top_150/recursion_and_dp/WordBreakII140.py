from typing import List
from collections import defaultdict


class WordBreakII:

    def generateSentence(self, s: str, wordDict: List[str]) -> List[str]:

        memo = defaultdict(list)

        wordSet = set(wordDict)

        def recurseWithMemo(s: str):

            if not s:
                return [[]]
            if s in memo:
                return memo[s]

            for i in range(1, len(s) + 1):
                if s[:i] in wordSet:
                    for seq in recurseWithMemo(s[i:]):
                        memo[s].append([s[:i]] + seq)
            return memo[s]

        recurseWithMemo(s)
        result = []
        for words in memo[s]:
            result.append(" ".join(words))
        return result


if __name__ == "__main__":
    wB = WordBreakII()
    print(wB.generateSentence(s="catsanddog", wordDict=["cat", "cats", "and", "sand", "dog"]))
