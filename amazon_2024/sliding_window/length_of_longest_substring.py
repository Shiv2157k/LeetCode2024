from typing import List


class ForbiddenString:

    def lengthOfLongestWithoutForbidden(self, s: str, forbidden: List[str]) -> int:
        """
        Approach: Sliding Window
        T: O(N * M**10)
        S: O(1)
        :param s:
        :param forbidden:
        :return:
        """

        forbidden = set(forbidden)
        left = maxLen = 0
        maxWindowLen = 0

        for word in forbidden:
            maxWindowLen = max(maxWindowLen, len(word))

        for right in range(len(s)):
            for pointer in range(right, max(right - maxWindowLen, left - 1), -1):

                if s[pointer: right + 1] in forbidden:
                    left = pointer + 1

            maxLen = max(maxLen, right - left + 1)
        return maxLen


if __name__ == "__main__":
    forbiddenString = ForbiddenString()
    print(forbiddenString.lengthOfLongestWithoutForbidden("cbaaaabc", ["aaa", "cb"]))
    print(forbiddenString.lengthOfLongestWithoutForbidden("leetcode", ["de", "le", "e"]))
