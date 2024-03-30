class Integer:

    def reverse_int(self, x: int) -> int:
        """
        Approach:
        T: O(N)
        S: O(1)
        :param x:
        :return:
        """

        result = 0
        sign = 1

        if x < 0:
            x = -x
            sign = -sign

        while x != 0:
            result = result * 10 + x % 10
            x = x // 10
        return 0 if result > 2 ** 31 else result * sign


if __name__ == "__main__":
    integer = Integer()
    print(integer.reverse_int(122331))
    print(integer.reverse_int(99999999999))
    print(integer.reverse_int(91))
