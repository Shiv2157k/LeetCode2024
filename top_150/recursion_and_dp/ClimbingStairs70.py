from typing import Dict


class Stairs:

    def climbWaysV3(self, n: int) -> int:
        """
        Approach: Factorial
        T: O(N)
        S: O(1)
        :param n:
        :return:
        """

        first = 1
        second = 2

        for num in range(3, n + 1):
            third = first + second
            first, second = second, third
        return second

    def climbWaysV2(self, n: int) -> int:
        """
        Approach: DP
        T: O(n)
        S: O(n)
        :param n:
        :return:
        """
        if n <= 2:
            return n
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for num in range(2, n):
            dp[num] = dp[num - 1] + dp[num - 2]
        return dp[-1]

    def climbWaysV1(self, n: int) -> int:
        """
        Approach: Recursion with Memo
        T: O(n)
        S: O(n)
        :param n:
        :return:
        """
        memo = {1: 1, 2: 2}
        return self._recurseWithMemo(n, memo)

    def _recurseWithMemo(self, n: int, memo: Dict):
        if n in memo:
            return memo[n]
        if n <= 0:
            return 0
        memo[n] = self._recurseWithMemo(n - 1, memo) + self._recurseWithMemo(n - 2, memo)
        return memo[n]

    def climbWaysV0(self, n: int) -> int:
        """
        Approach: Recursion
        T: O(n)
        S: O(n)
        :param n:
        :return:
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbWaysV0(n - 1) + self.climbWaysV0(n - 2)


if __name__ == "__main__":

    stairs = Stairs()
    print(stairs.climbWaysV0(5))
    print(stairs.climbWaysV1(5))
    print(stairs.climbWaysV2(5))
    print(stairs.climbWaysV3(5))