class DecodeWays:

    def totalWaysV2(self, s: str) -> int:
        """
        Approach: DP Without Space
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """
        length = len(s)
        if s[0] == "0":
            return 0
        if length == 1:
            return 1
        twoBack = 1
        oneBack = 0 if s[1] == "0" else 1

        for index in range(1, length):
            current = 0
            if s[index] != "0":
                current += oneBack
            if 10 <= int(s[index - 1: index + 1]) <= 26:
                current += twoBack
            twoBack, oneBack = oneBack, current
        return oneBack

    def totalWaysV1(self, s: str) -> int:
        """
        Approach: DP (Bottom - UP)
        T: O(N)
        S: O(N)
        :param s:
        :return:
        """

        length = len(s)
        if s[0] == "0":
            return 0
        if length == 1:
            return 1

        dp = [0] * (length + 1)
        dp[0] = 1
        dp[1] = 0 if s[1] == "0" else 1

        for index in range(1, length):
            if s[index] != "0":
                dp[index + 1] += dp[index]
            twoDigit = int(s[index - 1: index + 1])
            if 10 <= twoDigit <= 26:
                dp[index + 1] += dp[index - 1]
        return dp[-1]

    def totalWaysV0(self, s: str) -> int:
        """
        Approach: Recursion With Memo (Top Down)
        T: O()
        S: O()
        :param s:
        :return:
        """

        memo = {}

        def recurseWithMemo(pos: int, s: str) -> int:

            if pos == len(s):
                return 1
            if s[pos] == "0":
                return 0
            if pos in memo:
                return memo[pos]
            if pos == len(s) - 1:
                return 1

            ans = recurseWithMemo(pos + 1, s)
            if int(s[pos: pos + 2]) <= 26:
                ans += recurseWithMemo(pos + 2, s)
            memo[pos] = ans
            return ans

        return recurseWithMemo(0, s)


if __name__ == "__main__":
    decodeWays = DecodeWays()
    print(decodeWays.totalWaysV0("226"))
    print(decodeWays.totalWaysV1("226"))
    print(decodeWays.totalWaysV2("226"))
