class TwoWords:

    def editDistanceV2(self, word1: str, word2: str) -> int:
        """
        Approach: DP Tabulation (Bottom Up Approach)
        T: O(MN)
        S: O(MN
        :param word1:
        :param word2:
        :return:
        """
        w1, w2 = len(word1), len(word2)

        if w1 == 0:
            return w2
        if w2 == 0:
            return w1

        dp = [[0] * (w2 + 1) for _ in range(w1 + 1)]

        # add the upper and left grids
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

    def editDistanceV1(self, word1: str, word2: str) -> int:
        """
        Approach: Recursion With Memo (Top-Down Approach)
        T: O(M*N)
        S: O(M*N)
        :param word1:
        :param word2:
        :return:
        """
        w1, w2 = len(word1), len(word2)

        memo = [[0] * (w2 + 1) for _ in range(w1 + 1)]

        def recurseWithMemo(word1: str, word2: str, p1: int, p2: int):

            if p1 == 0:  # add
                return p2
            if p2 == 0:  # delete
                return p1
            if memo[p1][p2] != 0:
                return memo[p1][p2]

            minEditDistance = 0
            # if characters are equal,
            # skip and move to the next characters
            # in word1 and word2
            if word1[p1 - 1] == word2[p2 - 1]:
                minEditDistance = recurseWithMemo(word1, word2, p1 - 1, p2 - 1)
            else:  # otherwise: perform insert, delete and replace
                insert = recurseWithMemo(word1, word2, p1, p2 - 1)
                delete = recurseWithMemo(word1, word2, p1 - 1, p2)
                replace = recurseWithMemo(word1, word2, p1 - 1, p2 - 1)

                minEditDistance = min(insert, delete, replace) + 1
            memo[p1][p2] = minEditDistance
            return minEditDistance

        return recurseWithMemo(word1, word2, w1, w2)

    def editDistanceV0(self, word1: str, word2: str) -> int:
        """
        Approach: Recursion
        T: O(3^M)
        S: O(M)
        :param word1:
        :param word2:
        :return:
        """

        def recurse(word1: str, word2: str, p1: int, p2: int) -> int:
            # base cases
            if p1 == 0:  # add operation
                return p2
            if p2 == 0:  # delete operation
                return p1

            # if characters are equal,
            # skip and move to the next characters
            # in word1 and word2
            if word1[p1 - 1] == word2[p2 - 1]:
                return recurse(word1, word2, p1 - 1, p2 - 1)
            # otherwise: perform insert, delete and replace
            else:
                insert = recurse(word1, word2, p1, p2 - 1)
                delete = recurse(word1, word2, p1 - 1, p2)
                replace = recurse(word1, word2, p1 - 1, p2 - 1)
                return min(insert, delete, replace) + 1

        return recurse(word1, word2, len(word1), len(word2))


if __name__ == "__main__":
    twoWords = TwoWords()
    print(twoWords.editDistanceV0("horse", "ros"))
    print(twoWords.editDistanceV0("intention", "execution"))

    print(twoWords.editDistanceV1("horse", "ros"))
    print(twoWords.editDistanceV1("intention", "execution"))

    print(twoWords.editDistanceV2("horse", "ros"))
    print(twoWords.editDistanceV2("intention", "execution"))
