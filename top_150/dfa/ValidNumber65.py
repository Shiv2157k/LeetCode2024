

class ValidNumber:


    def isNumberV1(self, s: str) -> bool:
        """
        Approach: DFA
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """

        dfa = [
            {"digit": 1, "sign": 2, "dot": 3},
            {"digit": 1, "dot": 4, "exponent": 5},
            {"digit": 1, "dot": 3},
            {"digit": 4, "exponent": 5},
            {"sign": 6, "digit": 7},
            {"digit": 7},
            {"digit": 7}
        ]

        currState = 0

        for char in s:

            if char.isdigit():
                group = "digit"
            elif char in {"+", "-"}:
                group = "sign"
            elif char in {"e", "E"}:
                group = "exponent"
            elif char == ".":
                group = "dot"
            else:
                return False

            if group not in dfa[currState]:
                return False
            currState = dfa[currState][group]
        return currState in {1, 4, 7}

    def isNumberV0(self, s: str) -> bool:
        """
        Approach: Follow the rules
        T: O(N)
        S: O(1)
        :param s:
        :return:
        """

        seenDigit = False
        seenExponent = False
        seenDot = False

        for ptr, char in enumerate(s):

            if char.isdigit():
                seenDigit = True
            elif char in {'+', '-'}:
                if ptr > 0 and s[ptr - 1] != 'E' and s[ptr - 1] != 'e':
                    return False
            elif char in {'e', 'E'}:
                if seenExponent or not seenDigit:
                    return False
                seenExponent = True
                seenDigit = False
            elif char == '.':
                if seenDot or seenExponent:
                    return False
                seenDot = True
            else:
                return False
        return seenDigit

