class Atoi:

    def string_to_integer(self, s: str) -> int:
        """
        Approach: Linear
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """
        ptr = 0

        while ptr < len(s) and s[ptr].isspace():
            ptr += 1

        result = 0
        if ptr >= len(s):
            return result
        sign = 1

        if s[ptr] == '+':
            ptr += 1
        elif s[ptr] == '-':
            sign *= -1
            ptr += 1
        elif not s[ptr].isdigit():
            return result
        else:
            result += ord(s[ptr]) - ord('0')
            ptr += 1

        MAX_INT = 2 ** 31 - 1
        MIN_INT = 2 ** 31

        while ptr < len(s) and s[ptr].isdigit():
            result = (result * 10) + (ord(s[ptr]) - ord('0'))

            if sign < 0 and result >= MIN_INT:
                return sign * MIN_INT
            if sign > 0 and result >= MAX_INT:
                return MAX_INT
            ptr += 1
        return sign * result
