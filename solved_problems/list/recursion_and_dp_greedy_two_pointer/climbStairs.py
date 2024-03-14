from typing import List


class Stairs:

    def total_ways_to_climb(self, n: int) -> int:
        """
        Recursion
        T: O(n^2)
        S: O(n)
        :param n:
        :return:
        """

        def climb_stairs(i: int, n: int) -> int:

            if i > n:
                return 0
            if i == n:
                return 1
            return climb_stairs(i + 1, n) + climb_stairs(i + 2, n)

        return climb_stairs(0, n)

    def total_ways_to_climb_(self, n: int) -> int:
        """
        Recursion + Memoization
        T: O(N)
        S: O(N)
        :param n:
        :return:
        """

        def climb_stairs(i: int, n: int, memo: List[int]) -> int:

            if i > n:
                return 0
            if i == n:
                return 1
            if memo[i] > 0:
                return memo[i]
            memo[i] = climb_stairs(i + 1, n, memo) + climb_stairs(i + 2, n, memo)
            return memo[i]

        memo = [0 for i in range(n + 1)]
        return climb_stairs(0, n, memo)

    def total_ways_to_climb__(self, n: int) -> int:
        """
        Approach: Dynamic Programming
        T: O(N)
        S: O(N)
        :param n:
        :return:
        """
        if n == 1:
            return 1

        dp = [0 for i in range(n + 1)]
        dp[1], dp[2] = 1, 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def total_ways_to_climb____(self, n: int) -> int:
        """
        Fibonacci
        T: O(N)
        S:O(1)
        :param n:
        :return:
        """
        if n == 1:
            return 1
        first, second = 1, 2
        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third
        return second


if __name__ == "__main__":
    stairs = Stairs()
    print(stairs.total_ways_to_climb____(6))


