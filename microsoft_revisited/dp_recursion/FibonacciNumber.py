class FibonacciNumber:

    def get_fib(self, n: int):
        """
        Approach: DP no space
        T: O(N)
        S: O(1)
        :param n:
        :return:
        """

        if n < 2:
            return n

        first: int = 1
        second: int = 1

        for i in range(3, n + 1):
            third: int = first + second
            first, second = second, third
        return second
