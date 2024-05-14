class LongestCommonSubsequence:

    def longest_common_subsequence_v2(self, text1: str, text2: str) -> int:
        """
        Approach: DP with space optimization
        T: O(MN)
        S: O(1)
        :param text1:
        :param text2:
        :return:
        """

        if len(text2) < len(text1):
            text1, text2 = text2, text1

        previous = [0] * (len(text1) + 1)
        current = [0] * (len(text2) + 1)

        for col in range(len(text2) - 1, -1, -1):
            for row in range(len(text1) - 1, -1, -1):

                if text1[row] == text2[col]:
                    current[row] = 1 + previous[row + 1]
                else:
                    current[row] = max(current[row + 1], previous[row])
            previous, current = current, previous
        return previous[0]

    def longest_common_subsequence_v1(self, text1: str, text2: str) -> int:
        """
        Approach: DP with Tabulation
        T: O(MN)
        S: O(MN)
        :param text1:
        :param text2:
        :return:
        """
        t1_len = len(text1)
        t2_len = len(text2)

        dp = [[0] * (t2_len + 1) for _ in range(t1_len + 1)]

        for col in range(t2_len - 1, -1, -1):
            for row in range(t1_len - 1, -1, -1):

                if text2[col] == text1[row]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                else:
                    dp[row][col] = max(dp[row + 1][col], dp[row][col + 1])
        return dp[0][0]

    def longest_common_subsequence_v01(self, text1: str, text2: str) -> int:
        """
        Approach: Recursion with memo
        T: O(MN)
        S: O(MN)
        :param text1:
        :param text2:
        :return:
        """

        def helper(p1: int, p2: int) -> int:

            if p1 == len(text1) or p2 == len(text2):
                return 0

            if memo[p1][p2] != -1:
                return memo[p1][p2]

            result = 0
            if text1[p1] == text2[p2]:
                result = 1 + helper(p1 + 1, p2 + 1)
            else:
                result = max(helper(p1, p2 + 1), helper(p1 + 1, p2))
            memo[p1][p2] = result
            return memo[p1][p2]

        memo = [[-1] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        return helper(0, 0)

    def longest_common_subsequence_v0(self, text1: str, text2: str) -> int:
        """
        Approach: Recursion with memo
        T: O(MN)
        S: O(MN)
        :param text1:
        :param text2:
        :return:
        """

        def helper(p1: int, p2: int) -> int:
            # base case
            if p1 == len(text1) or p2 == len(text2):
                return 0

            if memo[p1][p2] != -1:
                return memo[p1][p2]

            option1 = helper(p1 + 1, p2)

            first_occurrence = text2.find(text1[p1], p2)
            option2 = 0

            if first_occurrence != -1:
                option2 = 1 + helper(p1 + 1, p2 + 1)
            memo[p1][p2] = max(option1, option2)
            return memo[p1][p2]

        memo = [[-1] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        return helper(0, 0)
