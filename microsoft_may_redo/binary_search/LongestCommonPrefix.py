from typing import List
from math import inf


class LongestCommonPrefix:

    def longest_common_prefix(self, strs: List[str]) -> str:
        """
        Approach: Binary Search
        T: O(S * log m)
        S: O(1)
        :param strs:
        :return:
        """

        if not strs:
            return ''

        left = 0
        right = inf

        for word in strs:
            right = min(right, len(word))

        while left <= right:
            pivot = left + (right - left) // 2
            if self.__is_common_prefix(strs, pivot):
                left = pivot + 1
            else:
                right = pivot - 1
        return strs[0][: (left + right) // 2]

    def __is_common_prefix(self, s: List[str], pivot: int) -> bool:

        char = s[0][:pivot]

        for i in range(1, len(s)):
            if not s[i].startswith(char):
                return False
        return True
