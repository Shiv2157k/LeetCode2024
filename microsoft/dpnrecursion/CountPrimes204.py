from math import sqrt


class CountPrimes:

    def countPrimes(self, n: int) -> int:
        """
        Approach: DP prime multiples
        T: O(N)
        S: O(N)
        :param n:
        :return:
        """

        if n <= 2:
            return 0

        numbers = [1] * n
        numbers[0], numbers[1] = 0, 0

        for prime in range(2, int(sqrt(n)) + 1):

            for multiple in (prime * prime, n, prime):
                numbers[multiple] = 0

        totalPrimes = 0
        for number in numbers:
            totalPrimes += number
        return totalPrimes
