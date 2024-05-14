class GreatestCommonDivisor:

    def gcd_of_strings(self, str1: str, str2: str) -> str:
        """
        Approach: Math
        t: O(log(min(m, n))
        S: O(log(min(m, n))
        :param str1:
        :param str2:
        :return:
        """

        def gcd(x: int, y: int):
            if y == 0:
                return x
            else:
                return gcd(y, x % y)

        if str1 + str2 != str2 + str1:
            return ""
        gcd_len = gcd(len(str1), len(str2))
        return str1[:gcd_len]
