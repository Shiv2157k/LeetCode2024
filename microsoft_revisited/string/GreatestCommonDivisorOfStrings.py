class GreatestCommonDivisor:

    def gcd_of_two_strings_v1(self, str1: str, str2: str) -> str:
        """
        Approach: Greatest Common Divisor
        T: O(M + N)
        S: O(M + N)
        :param str1:
        :param str2:
        :return:
        """

        # validation
        if str1 + str2 != str2 + str1:
            return ""

        def gcd(x: int, y: int):
            if y == 0:
                return x
            else:
                return gcd(y, x % y)

        max_len: int = gcd(len(str1), len(str2))
        return str1[: max_len]

    def gcd_of_two_strings_v0(self, str1: str, str2: str) -> str:

        n1, n2 = len(str1), len(str2)

        def is_divisor(l: int):
            if n1 % l or n2 % l:
                return False
            f1, f2 = n1 // l, n2 // l
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        for l in range(min(n1, n2), 0, -1):
            if is_divisor(l):
                return str1[:l]
        return ""
