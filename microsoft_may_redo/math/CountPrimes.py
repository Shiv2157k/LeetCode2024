from math import sqrt


class CountPrimes:

    def count_primes(self, n: int) -> int:
        """
        Approach: MAth
        T: O(sqrt(n) log * log n + n)
        S: O(N)
        :param n:
        :return:
        """

        if n <= 2:
            return 0

        numbers = [1] * n
        numbers[0] = 0
        numbers[1] = 0

        for prime in range(2, int(sqrt(n)) + 1):
            if numbers[prime] == 1:
                for multiple in range(prime * prime, n, prime):
                    numbers[multiple] = 0

        total_primes = 0
        for number in numbers:
            total_primes += number
        return total_primes
