


class Power:

    def ofXAndNV0(self, x: float, n: int) -> float:
        def recurse(x: float, n: int):

            if n == 0:
                return 1.0
            if n < 0:
                return 1.0 / recurse(x, -1 * n)
            if n % 2 == 1:
                return x * recurse(x * x, (n - 1) // 2)
            else:
                return recurse(x * x, n // 2)
        return recurse(x, n)

    def ofXAndNV1(self, x: float, n: int) -> float:

        if n == 0:
            return 1
        if n == 1:
            return x

        if n < 0:
            x = 1.0 / x
            n = -n

        result = 1
        while n != 0:
            if n % 2 == 1:
                result *= x
                n -= 1
            x *= x
            n //= 2
        return result


if __name__ == "__main__":
    power = Power()
    print(power.ofXAndNV1(2.0000, 10))
    print(power.ofXAndNV1(2.0000, -10))
    print(power.ofXAndNV1(2.0000, -2))

    print(power.ofXAndNV0(2.0000, 10))
    print(power.ofXAndNV0(2.0000, -10))
    print(power.ofXAndNV0(2.0000, -2))