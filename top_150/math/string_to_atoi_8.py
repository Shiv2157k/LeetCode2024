class Atoi:

    def stringToInteger(self, s: str) -> int:
        """
        Approach:
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """

        # strip the leading spaces
        s = s.strip()
        result = 0
        # validation
        if not s:
            return result

        sign = 1

        if s[0] == "+":
            sign = sign
        elif s[0] == "-":
            sign = -sign
        elif not s[0].isnumeric():
            return result
        else:
            result = ord(s[0]) - ord("0")

        INT_MAX = 2 ** 31 - 1
        INT_MIN = 2 ** 31

        for char in s[1:]:

            if char.isnumeric():
                result = result * 10 + ord(char) - ord("0")
                if sign > 0 and result >= INT_MAX:
                    return INT_MAX
                elif sign < 0 and result >= INT_MIN:
                    return -INT_MIN
            else:
                break

        return result * sign


if __name__ == "__main__":
    atoi = Atoi()
    print(atoi.stringToInteger("    +23"))
    print(atoi.stringToInteger("    -23"))
    print(atoi.stringToInteger("    00023zs"))
    print(atoi.stringToInteger("    000239 zs"))
    print(atoi.stringToInteger("2147483647"))
    print(atoi.stringToInteger("-214748364"))
    print(atoi.stringToInteger("9999999999999"))
