from typing import List
from collections import defaultdict


class WordII:

    def break_combinations(self, string: str, word_dict: List) -> List[str]:

        dp = defaultdict(list)
        # dp = {}
        word_set = set(word_dict)

        def _wordbreak_topdown(string: str):
            # base case
            if not string:
                return [[]]
            if string in dp:
                return dp[string]

            for end_index in range(1, len(string) + 1):
                word = string[:end_index]
                if word in word_set:
                    for subscentence in _wordbreak_topdown(string[end_index:]):
                        dp[string].append([word] + subscentence)
            return dp[string]

        _wordbreak_topdown(string)
        return [" ".join(words) for words in dp[string]]


if __name__ == "__main__":
    word_break = WordII()
    print(word_break.break_combinations(
        "catsanddog", ["cat", "cats", "and", "sand", "dog"]
    ))
