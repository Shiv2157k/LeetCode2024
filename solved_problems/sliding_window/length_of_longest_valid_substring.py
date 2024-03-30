from typing import List



class Forbidden:


    def longestValidSubstring(self, word: str, forbidden: List[str]) -> str:
        """
        Approach: Sliding Window
        T: O(N * M**10)
        S: O(1)
        :param word:
        :param forbidden:
        :return:
        """
        left = maxLen = 0
        maxWindowLen = 0
        for content in forbidden:
            maxWindowLen = max(maxWindowLen, len(content))

        for right in range(len(word)):
            for pointer in range(right, max(right - maxWindowLen, left - 1), -1):
                if word[pointer: right + 1] in forbidden:
                    left = pointer + 1
                    break
            maxLen = max(maxLen, right - left + 1)
        return maxLen


if __name__ == "__main__":
    forbid = Forbidden()
    print(forbid.longestValidSubstring("cbaaaabc", ["aaa", "cb"]))
    print(forbid.longestValidSubstring("leetcode", ["de", "le", "e"]))
