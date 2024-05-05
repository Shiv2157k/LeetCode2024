from typing import List


class LongestCommonSubSeq:

    def longest_common_subseq_v2(self, text1: str, text2: str) -> int:
        """
        Approach: DP with space optimization
        T: O(MN)
        S: O(N)
        :param text1:
        :param text2:
        :return:
        """

        if len(text1) < len(text2):
            text1, text2 = text2, text1

        previous = [0] * (len(text1) + 1)
        current = [0] * (len(text1) + 1)

        for col in range(len(text2) - 1, -1, -1):
            for row in range(len(text1) - 1, -1, -1):
                if text2[col] == text1[row]:
                    current[row] = 1 + previous[row + 1]
                else:
                    current[row] = max(previous[row], current[row + 1])
            previous, current = current, previous
        return previous[0]

    def longest_common_subseq_v1(self, text1: str, text2: str) -> int:
        """
        Approach: DP with tabulation
        T: O(MN)
        S: O(MN)
        :param text1:
        :param text2:
        :return:
        """

        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for col in range(len(text2) - 1, -1, -1):
            for row in range(len(text1) - 1, -1, -1):

                if text2[col] == text1[row]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                else:
                    dp[row][col] = max(dp[row + 1][col], dp[row][col + 1])
        return dp[0][0]

    def longest_common_subseq_v0(self, text1: str, text2: str) -> int:
        """
        Approach: Recursion with memoization
        T: O(MN^2)
        S: O(MN)
        :param text1:
        :param text2:
        :return:
        """

        def memo_solve(p1: int, p2: int):

            # base case
            if p1 == len(text1) or p2 == len(text2):
                return 0

            if memo[p1][p2] != -1:
                return memo[p1][p2]

            # case 1: we skip the 1st letter of text1
            case1 = memo_solve(p1 + 1, p2)

            # case2: include p1 from there is a match for it in text2
            first_occurrence = text2.find(text1[p1], p2)
            case2 = 0

            if first_occurrence != -1:
                case2 = 1 + memo_solve(p1 + 1, first_occurrence + 1)

            memo[p1][p2] = max(case1, case2)
            return memo[p1][p2]

        memo: List[List[int]] = [[-1] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        return memo_solve(0, 0)
