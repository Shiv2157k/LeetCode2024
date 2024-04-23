from typing import List, Dict, Tuple


class FizzBuzz:

    def fizz_buzz_v1(self, n: int) -> List[str]:
        """
        Approach: Hash Map
        T: O(N)
        S: O(N)
        :param n:
        :return:
        """
        result: List[str] = []
        fizz_buzz_map: Dict[int, str] = {
            3: 'Fizz', 5: 'Buzz'
        }
        divisors: Tuple[int, int] = (3, 5)

        for num in range(1, n + 1):
            curr: List[str] = []
            for divisor in divisors:
                if num % divisor == 0:
                    curr.append(fizz_buzz_map[divisor])
            if len(curr) == 0:
                curr.append(str(num))
            result.append(''.join(curr))
        return result

    def fizz_buzz_v0(self, n: int) -> List[str]:
        """
        Approach: Linear
        T: O(N)
        S: O(1)
        :param n:
        :return:
        """
        result: List[str] = []
        for i in range(1, n + 1):

            if i % 3 == 0 and i % 5 == 0:
                result.append('FizzBuzz')
            elif i % 5 == 0:
                result.append('Buzz')
            elif i % 3 == 0:
                result.append('Fizz')
            else:
                result.append(str(i))
        return result
