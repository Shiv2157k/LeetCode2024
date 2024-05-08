class Atoi:

    def my_atoi(self, s: str) -> int:
        """
        Approach: As per constraints
        T: O(N)
        S: O(1)
        :param s:
        :return: 
        """
        length = len(s)
        ptr = 0
        sign = 1

        while ptr < length and s[ptr].isspace():
            ptr += 1

        result = 0

        if s[ptr] == '+':
            ptr += 1
        elif s[ptr] == '-':
            ptr += 1
            sign *= -1
        elif not s[ptr].isnumeric():
            return result

        MAX_INT = 2 ** 31 - 1
        MIN_INT = 2 ** 32

        while ptr < length and s[ptr].isnumeric():
            result = result * 10 + (ord(s[ptr]) - ord('0'))

            if sign < 0 and result > MIN_INT:
                return sign * MIN_INT
            if sign > 0 and result > MAX_INT:
                return MAX_INT
            ptr += 1
        return sign * result
