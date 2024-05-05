from typing import List


class Strings:

    def is_interleaving_v2(self, s1: str, s2: str, s3: str) -> bool:
        """
        Approach: DP with O(N)
        T: O(MN)
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

    def is_interleaving_v1(self, s1: str, s2: str, s3: str) -> bool:
        """
        Approach: DP with tabulation
        T: O(M * N)
        S: O(M * N)
        :param s1:
        :param s2:
        :param s3:
        :return:
        """

        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True

        for p1 in range(1, len(s1) + 1):
            dp[p1][0] = dp[p1 - 1][0] and s1[p1 - 1] == s3[p1 - 1]

        for p2 in range(1, len(s2) + 1):
            dp[0][p2] = dp[p2 - 1][0] and s2[p2 - 1] == s3[p2 - 1]

        for p1 in range(1, len(s1) + 1):
            for p2 in range(1, len(s2) + 1):
                dp[p1][p2] = (dp[p1 - 1][p2] and s1[p1 - 1] == s3[p1 + p2 - 1]) or (
                        dp[p1][p2 - 1] and s2[p2 - 1] == s3[p1 + p2 - 1])
        return dp[-1][-1]

    def is_interleaving_v0(self, s1: str, s2: str, s3: str) -> bool:
        """
        Approach: Recursion with memoization
        T: O(N)
        S: O()
        :param s1:
        :param s2:
        :param s3:
        :return:
        """
        if len(s1) + len(s2) != len(s3):
            return False

        def helper(p1: int, p2: int, p3: int):

            if p1 == len(s1):
                return s2[p2:] == s3[p3:]
            if p2 == len(s2):
                return s1[p1:] == s3[p3:]
            if memo[p1][p2] != -1:
                return memo[p1][p2] == 1

            is_interleave = False

            if (s1[p1] == s3[p3] and helper(p1 + 1, p2, p3 + 1)) or (s2[p2] == s3[p3] and helper(p1, p2 + 1, p3 + 1)):
                is_interleave = True

            memo[p1][p2] = 1 if is_interleave else 0
            return is_interleave

        memo = [[-1] * len(s2) for _ in range(len(s1))]
        return helper(0, 0, 0)
