from typing import List


class PalindromePartition:

    def minCut(self, s: str) -> int:

        cutsDp = [0] * len(s)

        for i in range(1, len(s)):
            cutsDp[i] = i

        for mid in range(0, len(s)):
            self._findMinimumCut(s, mid, mid, cutsDp)
            self._findMinimumCut(s, mid, mid + 1, cutsDp)
        return cutsDp[-1]

    def _findMinimumCut(self, s: str, left: int, right: int, cutsDp: List[List[int]]) -> None:

        while left >= 0 and right < len(s) and s[left] == s[right]:
            minCut = 0 if left == 0 else cutsDp[left - 1] + 1
            cutsDp[right] = min(cutsDp[right], minCut)
            left -= 1
            right += 1


if __name__ == "__main__":
    palindromePartition = PalindromePartition()
    print(palindromePartition.minCut("aab"))
    print(palindromePartition.minCut("nooradars"))
