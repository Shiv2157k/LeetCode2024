class PowerOfXN:

    def binary_exp_iterative(self, x: float, n: int) -> float:
        """
        Approach: Math
        T: O(log N)
        S: O(1)
        :param x:
        :param n:
        :return:
        """

        result = 1
        if n == 0:
            return result

        if n < 0:
            n *= -1
            x = 1.0 / x

        while n:

            if n % 2 == 1:
                result *= x
                n -= 1

            x *= x
            n //= 2
        return result
