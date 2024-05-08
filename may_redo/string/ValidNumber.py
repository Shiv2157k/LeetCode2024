


class ValidNumber:


    def is_number(self, s: str) -> bool:
        """
        Approach: As per constraints
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """
        # will reset after exponent is encountered
        seen_digit = False
        # cannot be more than one dot
        seen_dot = False
        # sign -63e+7
        seen_exponent = False

        for ptr, val in enumerate(s):

            if val.isdigit():
                seen_digit = True
            elif val in {'+', '-'}:

                if ptr > 0 and s[ptr - 1] != 'e' or s[ptr - 1] != 'E':
                    return False
            elif val in {'e', 'E'}:
                if seen_dot or seen_exponent:
                    return False
                seen_exponent = True
                seen_digit = False
            elif val == '.':
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            else:
                return False
        return seen_digit
