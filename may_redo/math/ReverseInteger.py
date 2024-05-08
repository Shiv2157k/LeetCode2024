

class ReverseInteger:


    def reverse(self, x: int) -> int:
        """
        Approach: Math
        T: O(N)
        S: O(1)
        :param x:
        :return:
        """

        rev = 0
        sign = 1

        if x < 0:
            sign *= -1
            x *= sign

        while x != 0:
            rev = rev * 10 + x % 10
            x //= 10
        return 0 if x > 2**31 else rev * sign