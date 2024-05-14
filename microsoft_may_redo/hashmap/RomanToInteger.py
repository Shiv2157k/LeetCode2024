class RomanToInteger:

    def roman_to_int(self, s: str) -> int:
        """
        Approach: HashMap
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """

        roman_map = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }

        ptr = 0
        digit = 0
        # IV
        while ptr < len(s):

            if ptr < len(s) - 1 and roman_map[s[ptr]] < roman_map[s[ptr + 1]]:
                digit = digit + (roman_map[s[ptr + 1]] - roman_map[s[ptr]])
                ptr += 1
            else:
                digit += roman_map[s[ptr]]
            ptr += 1
        return digit
