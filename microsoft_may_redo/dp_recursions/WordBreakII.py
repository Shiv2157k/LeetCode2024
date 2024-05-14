from typing import List


class WordBreakII:

    def word_break_ii(self, s: str, word_list: List[str]) -> List[str]:
        """
        Approach: Recursion with memoization
        T: O(N^2 + 2^N + W)
        S: O(2^N * N + W)
        :param s:
        :param word_list:
        :return:
        """

        memo = {}
        word_set = set(word_list)

        def helper(s: str):

            if not s:
                return [[]]
            if s in memo:
                return memo[s]

            for i in range(1, len(s) + 1):
                if s[:i] in word_set:
                    if s not in memo:
                        memo[s] = []
                    for sub_seq in helper(s[i:]):
                        memo[s].append([s[:i]] + sub_seq)
            return memo.get(s, [])

        helper(s)
        result = []
        if s in memo:
            for words in memo[s]:
                result.append(" ".join(words))
        return result
