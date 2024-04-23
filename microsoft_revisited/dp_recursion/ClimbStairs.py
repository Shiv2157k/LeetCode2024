class ClimbStairs:

    def climbStairsV3(self, n: int) -> int:
        """
        Approach: DP
        T: O(N)
        S: O(1)
        :param n:
        :return:
        """
        if n <= 2:
            return n

        first = 1
        second = 2

        for num in range(3, n + 1):
            third = first + second
            first, second = second, third
        return second

    def climbStairsV2(self, n: int) -> int:
        """
        Approach: DP with space
        T: O(N)
        S: O(N)
        :param n:
        :return:
        """
        if n <= 2:
            return n
        dp = [0] * n
        dp[0], dp[1] = 1, 2

        for num in range(3, n + 1):
            dp[num - 1] = dp[num - 2] + dp[num - 3]
        return dp[-1]

    def climbStairs(self, n: int) -> int:
        """
        Approach: Recurse with memo
        T: O(N)
        S: O(N)
        :param n:
        :return:
        """

        memo = {}
        def recurseWithMemo(n: int) -> int:
            nonlocal memo
            if n <= 2:
                return n

            if n in memo:
                return memo[n]

            memo[n] = recurseWithMemo(n - 1) + recurseWithMemo(n - 2)
            return memo[n]
        return recurseWithMemo(n)

