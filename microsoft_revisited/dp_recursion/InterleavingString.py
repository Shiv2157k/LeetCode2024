from typing import List


class InterLeavingString:

    def isInterLeaveV2(self, s1: str, s2: str, s3: str) -> bool:
        """
        Approach: DP
        T: O(M * N)
        S: O(N)
        :param s1:
        :param s2:
        :param s3:
        :return:
        """

        if len(s1) + len(s2) != len(s3):
            return False

        dp = [False] * (len(s2) + 1)
        dp[0] = True

        for p2 in range(1, len(s2) + 1):
            dp[p2] = dp[p2 - 1] and s2[p2 - 1] == s3[p2 - 1]

        for p1 in range(1, len(s1) + 1):
            dp[0] = (dp[0] and s1[p1 - 1] == s3[p1 - 1])
            for p2 in range(1, len(s2) + 1):
                dp[p2] = (dp[p2] and s1[p1 - 1] == s3[p1 + p2 - 1]) or (dp[p2 - 1] and s2[p2 - 1] == s3[p1 + p2 - 1])
        return dp[-1]

    def isInterLeaveV1(self, s1: str, s2: str, s3: str) -> bool:
        """
        Approach: DP
        T: O(M * N)
        S: O(M * N)
        :param s1:
        :param s2:
        :param s3:
        :return:
        """

        # validation
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True

        for p1 in range(1, len(s1) + 1):
            dp[p1][0] = dp[p1 - 1][0] and s1[p1 - 1] == s3[p1 - 1]

        for p2 in range(1, len(s2) + 1):
            dp[0][p2] = dp[0][p2 - 1] and s2[p2 - 1] == s3[p2 - 1]

        for p1 in range(1, len(s1) + 1):
            for p2 in range(1, len(s2) + 1):
                dp[p1][p2] = (dp[p1 - 1][p2] and s1[p1 - 1] == s3[p1 + p2 - 1]) or (
                        dp[p1][p2 - 1] and s2[p2 - 1] == s3[p1 + p2 - 1])
        return dp[-1][-1]

    def isInterLeaveV0(self, s1: str, s2: str, s3: str) -> bool:
        """
        Approach: Recursion with memo
        T: O(M * N)
        S: O(M * N)
        :param s1:
        :param s2:
        :param s3:
        :return:
        """
        # validation
        if len(s1) + len(s2) != len(s3):
            return False

        memo = [[-1] * len(s2) for _ in range(len(s1))]
        return self._checkInterLeave(s1, 0, s2, 0, s3, 0, memo)

    def _checkInterLeave(self, s1: str, p1: int, s2: str, p2: int, s3: str, p3: int, memo: List[List[int]]) -> bool:

        if p1 == len(s1):
            return s2[p2:] == s3[p3:]
        if p2 == len(s2):
            return s1[p1:] == s3[p3:]

        if memo[p1][p2] >= 0:
            return True if memo[p1][p2] == 1 else False

        ans = False

        if (s3[p3] == s1[p1] and self._checkInterLeave(s1, p1 + 1, s2, p2, s3, p3 + 1, memo)) or (
                s3[p3] == s2[p2] and self._checkInterLeave(s1, p1, s2, p2 + 1, s3, p3 + 1, memo)):
            ans = True

        memo[p1][p2] = ans
