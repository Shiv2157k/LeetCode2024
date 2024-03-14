

class Exponent:

    def binary_exp(self, x: float, n: float) -> float:

        # base case
        if n == 0:
            return 1
        # if n is negative
        if n < 0:
            return 1.0 / self.binary_exp(x, -1 * n)

        # odd
        # we perform binary exponentiation on n - 1
        # multiplying with x
        if n % 2 == 1:
            return x * self.binary_exp(x * x, (n - 1) // 2)
        else:  # otherwise we calculate binary exponentiation on x
            return self.binary_exp(x * x, n // 2)

    def pow_of_xn(self, x: float, n: float) -> float:
        """
        Approach: Binary Exponential Recursion
        T: O(log N)
        S: O(log N)
        :param x:
        :param n:
        :return:
        """
        return self.binary_exp(x, n)

    def iterative_binary_exp(self, x: float, n: float) -> float:
        result = 1
        if n == 0:
            return 1
        if n < 0:
            n = -1 * n
            x = 1.0 / x
        while n != 0:

            if n % 2 == 1:
                result = result * x
                n -= 1
            x *= x
            n //= 2
        return result

    def pox_of_xn_v1(self, x: float, n: float) -> float:
        """
        Approach: Binary Exponential Iteration
        T:O(log N)
        S: O(1)
        :param x:
        :param n:
        :return:
        """
        return self.iterative_binary_exp(x, n)


if __name__ == "__main__":
    exponent = Exponent()
    print(exponent.pox_of_xn_v1(2, 10))
    print(exponent.pow_of_xn(2, 10))
    print(exponent.pox_of_xn_v1(2, -10))
    print(exponent.pow_of_xn(2, -10))
    print(exponent.pox_of_xn_v1(2, -3))
    print(exponent.pow_of_xn(2, 3))

