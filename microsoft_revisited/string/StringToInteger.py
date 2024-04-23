class Atoi:

    def myAtoi(self, s: str) -> int:
        """
        Approach: Go as per rule
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """

        # remove leading space
        # s = s.strip()
        ptr = 0
        while ptr < len(s) and s[ptr].isspace():  # s[ptr] == ' ':
            ptr += 1

        result = 0
        if ptr >= len(s):
            return result
        sign = 1

        if s[ptr] == '+':
            ptr += 1
        elif s[ptr] == '-':
            ptr += 1
            sign *= -1
        elif s[ptr].isnumeric():
            return result
        else:
            result += ord(s[ptr]) - ord('0')
            ptr += 1

        MAX_INT = 2 ** 31 - 1
        MIN_INT = 2 ** 31

        while ptr < len(s) and s[ptr].isnumeric():

            result = (result * 10) + (ord(s[ptr]) - ord('0'))

            if sign < 0 and result >= MIN_INT:
                return -MIN_INT
            elif sign > 0 and result >= MAX_INT:
                return MAX_INT
            ptr += 1

        return sign * result
