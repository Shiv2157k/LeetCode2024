from typing import List


class WordBreakII:

    def word_break(self, s: str, wordDict: List[str]) -> List[str]:
        """
        Approach: Recurse with memo
        T: O(N^2 + 2^N + W)
        S: O(2^N * N + W)
        :param s:
        :param wordDict:
        :return:
        """

        memo = {}
        word_set = set(wordDict)

        def recurse_with_memo(s: str) -> List[List[str]]:

            if not s:
                return [[]]
            if s in memo:
                return memo[s]

            for i in range(1, len(s) + 1):
                if s[:i] in word_set:
                    if s not in memo:
                        memo[s] = []
                    for sub_seq in recurse_with_memo(s[i:]):
                        memo[s].append([s[:i]] + sub_seq)
            return memo.get(s, [])

        recurse_with_memo(s)
        result = []
        if s in memo:
            for words in memo[s]:
                result.append(" ".join(words))
        return result
