from typing import Dict


class DecodeWays:

    def numbDecodingV2(self, s: str) -> int:
        """
        Approach: DP
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """
        if s[0] == '0':
            return 0
        length = len(s)
        if length == 1:
            return 1

        first = 1
        second = 1 if s[1] != '0' else 0

        for i in range(1, length):
            third = 0
            if s[i] != '0':
                third += second
            twoDigit = int(s[i - 1: i + 1])
            if 9 < twoDigit <= 26:
                third += first
            first, second = second, third
        return second

    def numbDecodingV1(self, s: str) -> int:
        """
        Approach: DP
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """
        if s[0] == '0':
            return 0

        length = len(s)
        if length == 1:
            return 1

        dp = [0] * (length + 1)
        dp[0] = 1
        dp[1] = 0 if s[1] == '0' else 1

        for i in range(1, length):

            if s[i] != '0':
                dp[i + 1] += dp[i]
            twoDigit = int(s[i - 1: i + 1])
            if 9 < twoDigit <= 26:
                dp[i + 1] += dp[i - 1]
        return dp[-1]

    def numbDecodingV0(self, s: str) -> int:
        """
        Approach: Recurse with memoization
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """
        memo = {}
        return self._recurseWithMemo(0, s, memo)

    def _recurseWithMemo(self, pos: int, s: str, memo: Dict[int, int]) -> int:

        if pos == len(s):
            return 1
        if s[pos] == '0':
            return 0
        if pos in memo:
            return memo[pos]
        if pos == len(s) - 1:
            return 1

        answer = self._recurseWithMemo(pos + 1, s, memo)
        if int(s[pos: pos + 2]) <= 26:
            answer += self._recurseWithMemo(pos + 2, s, memo)
        memo[pos] = answer
        return answer
