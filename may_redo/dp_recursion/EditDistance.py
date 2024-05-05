class EditDistance:

    def min_distance_v2(self, word1: str, word2: str) -> int:
        """
        Approach: DP Tabulation
        T: O(MN)
        S: O(MN)
        :param word1:
        :param word2:
        :return:
        """
        w1 = len(word1)
        w2 = len(word2)

        dp = [[0] * (w2 + 1) for _ in range(w1 + 1)]

        for p1 in range(1, w1 + 1):
            dp[p1][0] = p1

        for p2 in range(1, w2 + 1):
            dp[0][p2] = p2

        for p1 in range(1, w1 + 1):
            for p2 in range(1, w2 + 1):
                if word1[p1 - 1] == word2[p2 - 1]:
                    dp[p1][p2] = dp[p1 - 1][p2 - 1]
                else:
                    dp[p1][p2] = min(dp[p1 - 1][p2], dp[p1][p2 - 1], dp[p1 - 1][p2 - 1]) + 1
        return dp[w1][w2]

    def min_distance_v1(self, word1: str, word2: str) -> int:
        """
        Approach: Recurse with memo
        T: O(MN)
        S: O(MN)
        :param word1:
        :param word2:
        :return:
        """

        def recurse_with_memo(p1: int, p2: int) -> int:

            if p1 == 0:
                return p2
            if p2 == 0:
                return p1
            if memo[p1][p2] != 0:
                return memo[p1][p2]

            min_edit_distance = 0

            if word1[p1 - 1] == word2[p2 - 1]:
                min_edit_distance = recurse_with_memo(p1 - 1, p2 - 1)
            else:
                insert = recurse_with_memo(p1, p2 - 1)
                delete = recurse_with_memo(p1 - 1, p2)
                replace = recurse_with_memo(p1 - 1, p2 - 1)

                min_edit_distance = min(insert, delete, replace) + 1
            memo[p1][p2] = min_edit_distance
            return min_edit_distance

        memo = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        return recurse_with_memo(len(word1), len(word2))

    def min_distance_v0(self, word1: str, word2: str) -> int:
        """
        Approach: Pure recursion
        T: O(3^M)
        S: O(M)
        :param word1:
        :param word2:
        :return:
        """

        def recurse(p1: int, p2: int):

            if p1 == 0:
                return p2  # these many insert operations
            if p2 == 0:
                return p1  # these many delete operations

            if word1[p1 - 1] == word2[p1 - 1]:
                return recurse(p1 - 1, p2 - 1)
            else:
                insert = recurse(p1, p2 - 1)
                delete = recurse(p1 - 1, p2)
                replace = recurse(p1 - 1, p2 - 1)

                return min(insert, delete, replace) + 1

        return recurse(len(word1), len(word2))
