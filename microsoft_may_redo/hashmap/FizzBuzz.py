from typing import List


class FizzBuzz:

    def fizz_buzz(self, n: int) -> List[str]:
        """
        Approach: Advanced using HashMap
        T: O(N)
        S: O(1)
        :param n:
        :return:
        """

        result = []
        name_map = {
            3: 'Fizz',
            5: 'Buzz'
        }
        divisors = (3, 5)

        for num in range(1, n + 1):
            curr = []

            for divisor in divisors:
                if num % divisor == 0:
                    curr.append(name_map[divisor])
            if len(curr) == 0:
                curr.append(str(num))
            result.append(''.join(curr))
        return result
