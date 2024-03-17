from typing import List


class FizzBuzz:

    def generate_v2(self, n: int) -> List[int]:
        """
        Approach: Hash Map
        :param n:
        :return:
        """
        result = []
        fizz_buzz_map = {
            3: "Fizz",
            5: "Buzz"
        }
        divisor = [3, 5]

        for num in range(1, n + 1):
            ans = []
            for key in divisor:
                if num % key == 0:
                    ans.append(fizz_buzz_map[key])
            if not ans:
                ans.append(str(num))
            result.append("".join(ans))
        return result

    def generate_v1(self, n: int) -> List[int]:
        """
        Approach: String Concatention
        :param n:
        :return:
        """
        result = []

        for num in range(1, n + 1):
            div_by_3 = (num % 3 == 0)
            div_by_5 = (num % 5 == 0)

            ans = ""
            if div_by_3:
                ans += "Fizz"
            if div_by_5:
                ans += "Buzz"
            if not ans:
                ans += str(num)
            result.append(ans)
        return result

    def generate_v0(self, n: int) -> List[int]:
        """
        Approach: Linear
        :param n:
        :return:
        """
        result = []

        for num in range(1, n + 1):
            if num % 3 == 0 and num % 5 == 0:
                result.append("FizzBuzz")
            elif num % 5 == 0:
                result.append("Buzz")
            elif num % 3 == 0:
                result.append("Fizz")
            else:
                result.append(str(num))
        return result


if __name__ == "__main__":
    fizz_buzz = FizzBuzz()
    print(fizz_buzz.generate_v0(15))
    print(fizz_buzz.generate_v1(15))
    print(fizz_buzz.generate_v2(15))
