from typing import List


class LongestCommonPrefix:

    def find(self, strs: List[str]) -> str:
        """
        Approach: Binary Search
        T: O(log M)
        S: O(1)
        :param strs:
        :return:
        """

        if not strs:
            return strs

        left = 0
        right = float("inf")
        for word in strs:
            right = min(right, len(word))

        while left <= right:

            pivot = left + (right - left) // 2

            if self._isCommonPrefix(strs, pivot):
                left = pivot + 1
            else:
                right = pivot - 1

        return strs[0][0: (left + right) // 2]

    def _isCommonPrefix(self, s: List[str], length: int) -> bool:
        prefix = s[0][:length]
        for index in range(1, len(s)):
            if not s[index].startswith(prefix):
                return False
        return True


if __name__ == "__main__":
    longestCommonPrefix = LongestCommonPrefix()
    print(longestCommonPrefix.find(["flower", "flow", "flight"]))
    print(longestCommonPrefix.find(["dog", "racecar", "car"]))
    print(longestCommonPrefix.find(["clogg", "clogging", "clogger"]))
