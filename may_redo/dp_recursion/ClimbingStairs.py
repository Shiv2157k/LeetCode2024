class ClimbingStairs:

    def climb_stairs(self, n: int) -> int:
        """
        Approach: DP with no space
        T: O(N)
        S: O(1)
        :param n:
        :return:
        """

        if n <= 2:
            return n

        first = 1
        second = 2

        for i in range(3, n + 1):
            third = first + second
            first, second = second, third
        return second
