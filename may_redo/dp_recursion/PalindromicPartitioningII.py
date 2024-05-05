from typing import List


class PalindromicPartitioning:

    def min_cut(self, s: str) -> int:
        """
        Approach: Expand Center with DP
        T: O(N^2)
        S: O(N)
        :param s:
        :return:
        """

        cuts_dp = [0] * len(s)
        for i in range(1, len(s)):
            cuts_dp[i] = i

        for mid in range(len(s)):
            self._find_min_cuts(mid, mid, cuts_dp, s)
            self._find_min_cuts(mid, mid + 1, cuts_dp, s)
        return cuts_dp[-1]

    def _find_min_cuts(self, left: int, right: int, cuts_dp: List[int], s: str) -> None:
        """

        :param left:
        :param right:
        :param cuts_dp:
        :param s:
        :return:
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if left != 0:
                min_cut = cuts_dp[left - 1] + 1
            else:
                min_cut = 0
            cuts_dp[right] = min(cuts_dp[right], min_cut)
            left -= 1
            right += 1
